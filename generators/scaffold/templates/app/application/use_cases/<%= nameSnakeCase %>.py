from django_injector import inject

from application.repositories import <%= namePascalCase %>Repository


class <%= namePascalCase %>UseCase:
    @inject
    def __init__(self, <%= nameSnakeCase %>_repository: <%= namePascalCase %>Repository):
        self.<%= nameSnakeCase %>_repository = <%= nameSnakeCase %>_repository

    def watch_<%= nameSnakeCase %>(self, <%= nameSnakeCase %>_id: int) -> int:
        <%= nameSnakeCase %> = self.<%= nameSnakeCase %>_repository.get_by_id(<%= nameSnakeCase %>_id)
        <%= nameSnakeCase %>.view_count += 1
        return self.<%= nameSnakeCase %>_repository.save(<%= nameSnakeCase %>).view_count
