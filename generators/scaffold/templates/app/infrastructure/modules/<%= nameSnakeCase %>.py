from injector import Module, singleton, provider

from application.repositories import <%= namePascalCase %>Repository
from application.use_cases.<%= nameSnakeCase %> import <%= namePascalCase %>UseCase
from infrastructure.repositories.<%= nameSnakeCase %> import Django<%= namePascalCase %>Repository


class <%= namePascalCase %>Module(Module):

    @singleton
    @provider
    def <%= nameSnakeCase %>_repository(self) -> <%= namePascalCase %>Repository:
        return Django<%= namePascalCase %>Repository()

    # @singleton
    # @provider
    # def <%= nameSnakeCase %>_use_case(self, <%= nameSnakeCase %>_repository: <%= namePascalCase %>Repository):
    #     return <%= namePascalCase %>UseCase(<%= nameSnakeCase %>_repository)
