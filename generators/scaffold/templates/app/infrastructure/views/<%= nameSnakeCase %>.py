from http import HTTPStatus

from django_injector import inject

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from application.use_cases.<%= nameSnakeCase %> import <%= namePascalCase %>UseCase


class <%= namePascalCase %>ViewsAPI(APIView):
    
    # Handles both 'GET <%= nameSnakeCase %>s/<int:<%= nameSnakeCase %>_id>' and 'GET <%= nameSnakeCase %>s/' paths
    @inject
    def get(self, request: Request, <%= nameSnakeCase %>_id: int, <%= nameSnakeCase %>_use_case: <%= namePascalCase %>UseCase, format=None):
        print(request.META)
        print(request.data)
        print('<%= nameSnakeCase %>_id:', <%= nameSnakeCase %>_id)
        return Response(
            # data={'message': 'Get Request'},
            data=<%= nameSnakeCase %>_use_case.get_by_id(<%= nameSnakeCase %>_id),
            status=HTTPStatus.OK
        )

    def post(self, request: Request, format=None):
        print(request.META)
        print(request.data)
        return Response(
            data={'message': 'Post Request'},
            status=HTTPStatus.CREATED
        )

    def put(self, request: Request, format=None):
        print(request.META)
        print(request.data)
        return Response(
            data={'message': 'Post Request'},
            status=HTTPStatus.OK
        )

    def delete(self, request: Request, format=None):
        print(request.META)
        print(request.data)
        return Response(
            status=HTTPStatus.NO_CONTENT
        )
