from django.db import models

from domain import <%= namePascalCase %>
from infrastructure.models import BaseManager, BaseModel


class <%= namePascalCase %>Manager(BaseManager):

    def from_entity(self, entity: <%= namePascalCase %>):
        entity_dict = {
            "id": entity.id,
            "name": entity.name,
            "duration": entity.duration,
            "view_count": entity.view_count,
            "created_timestamp": entity.created_timestamp,
            "last_modified_timestamp": entity.last_modified_timestamp,
        }
        <%= name %>_model = self.model(**entity_dict)

        return <%= name %>_model


class <%= namePascalCase %>Model(BaseModel):
    objects = <%= namePascalCase %>Manager()
    
    name = models.CharField(max_length=1024)
    duration = models.IntegerField()
    view_count = models.IntegerField()

    def to_entity(self):
        entity_dict = {
            "id": self.id,
            "name": self.name,
            "duration": self.duration,
            "view_count": self.view_count,
            "created_timestamp": self.created_timestamp,
            "last_modified_timestamp": self.last_modified_timestamp,
        }

        return <%= namePascalCase %>(**entity_dict)

    def __str__(self):
        return self.name