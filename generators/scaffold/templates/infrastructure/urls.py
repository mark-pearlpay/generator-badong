from django.urls import path, include
from rest_framework.routers import SimpleRouter

from infrastructure.views import <%= namePascalCase %>ViewSet
from infrastructure.views.<%= nameSnakeCase %> import <%= namePascalCase %>ViewsAPI


class OptionalSlashRouter(SimpleRouter):

    def __init__(self):
        self.trailing_slash = '/?'
        super(SimpleRouter, self).__init__()


router = OptionalSlashRouter()
router.register('<%= nameDashSeparated %>', <%= namePascalCase %>ViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<%= nameDashSeparated %>/<int:<%= nameSnakeCase %>_id>/increment-view', <%= namePascalCase %>ViewsAPI.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
