from django.db import models

from domain import <%= namePascalCase %>


class <%= namePascalCase %>Model(models.Model):
    name = models.CharField(max_length=1024)
    duration = models.IntegerField()
    view_count = models.IntegerField()

    def to_entity(self):
        entity_dict = {
            "id": self.id,
            "name": self.name,
            "duration": self.duration,
            "view_count": self.view_count
        }

        return <%= namePascalCase %>(**entity_dict)

    def __str__(self):
        return self.name