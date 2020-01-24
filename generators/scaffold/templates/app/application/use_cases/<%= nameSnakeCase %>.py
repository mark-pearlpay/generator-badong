from django_injector import inject

from application.repositories import <%= namePascalCase %>Repository


class <%= namePascalCase %>UseCase:
	@inject
	def __init__(self, <%= nameSnakeCase %>_repository: <%= namePascalCase %>Repository):
		self.<%= nameSnakeCase %>_repository = <%= nameSnakeCase %>_repository

	def get_by_id(self, <%= nameSnakeCase %>_id: int):
		return self.<%= nameSnakeCase %>_repository.get_by_id(<%= nameSnakeCase %>_id)
