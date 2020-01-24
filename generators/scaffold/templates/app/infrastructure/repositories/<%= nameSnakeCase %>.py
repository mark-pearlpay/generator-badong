from dataclasses import asdict

from application.repositories import <%= namePascalCase %>Repository
from domain import <%= namePascalCase %>
from infrastructure.models import <%= namePascalCase %>Model


class Django<%= namePascalCase %>Repository(<%= namePascalCase %>Repository):

    @staticmethod
    def _get_<%= nameSnakeCase %>_model_by_id(<%= nameSnakeCase %>_id):
        return <%= namePascalCase %>Model.objects.get(id=<%= nameSnakeCase %>_id)

    def get_by_id(self, <%= nameSnakeCase %>_id) -> <%= namePascalCase %>:
        return Django<%= namePascalCase %>Repository._get_<%= nameSnakeCase %>_model_by_id(<%= nameSnakeCase %>_id).to_entity()

    def save(self, <%= nameSnakeCase %>: <%= namePascalCase %>) -> <%= namePascalCase %>:
        <%= nameSnakeCase %>_model = <%= namePascalCase %>Model.objects.from_entity(<%= nameSnakeCase %>)
        <%= nameSnakeCase %>_model.save()
        return <%= nameSnakeCase %>_model.to_entity()

    def update(self, <%= nameSnakeCase %>: <%= namePascalCase %>) -> <%= namePascalCase %>:
        <%= nameSnakeCase %>_model = Django<%= namePascalCase %>Repository._get_<%= nameSnakeCase %>_model_by_id(<%= nameSnakeCase %>.id)
        for key, value in asdict(<%= nameSnakeCase %>).items():
            setattr(<%= nameSnakeCase %>_model, key, value)
        <%= nameSnakeCase %>_model.save()
        return <%= nameSnakeCase %>_model.to_entity()
