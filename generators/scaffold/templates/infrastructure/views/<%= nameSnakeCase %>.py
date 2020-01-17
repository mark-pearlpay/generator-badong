from http import HTTPStatus

from django_injector import inject
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from application.use_cases.<%= nameSnakeCase %> import <%= namePascalCase %>UseCase
from infrastructure.models import <%= namePascalCase %>Model
from infrastructure.serializers import <%= namePascalCase %>Serializer


class <%= namePascalCase %>ViewSet(viewsets.ModelViewSet):
    queryset = <%= namePascalCase %>Model.objects.all().order_by('name')
    serializer_class = <%= namePascalCase %>Serializer


class <%= namePascalCase %>ViewsAPI(APIView):

    @inject
    def get(self, request: Request, <%= nameSnakeCase %>_id: int, <%= nameSnakeCase %>_use_case: <%= namePascalCase %>UseCase, format=None):
        current_view_count = <%= nameSnakeCase %>_use_case.watch_<%= nameSnakeCase %>(<%= nameSnakeCase %>_id)
        return Response(data={'current_view_count': current_view_count},
                        status=HTTPStatus.OK)
