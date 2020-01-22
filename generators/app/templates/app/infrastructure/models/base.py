from abc import abstractmethod, ABC

from django.db import models

# def filter_fields(data_dict: Dict, expected_fields: Iterable[str]):
#     print("data_dict", data_dict)
#     print("expected_fields", expected_fields)
#     filtered_dict = {key: value for key, value in data_dict.items() if key in expected_fields}
#     print("filtered", filtered_dict)
#     print()
#     return filtered_dict
from django.utils import timezone


class BaseManager(ABC, models.Manager):
    @abstractmethod
    def from_entity(self, entity):
        # model = self.model(**filter_fields(asdict(entity), self.model.get_fields()))
        # return model
        raise NotImplementedError()


class BaseModel(models.Model):
    # objects = BaseManager()

    created_timestamp = models.DateTimeField(editable=False)
    last_modified_timestamp = models.DateTimeField()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.id:
            self.created_timestamp = timezone.now()
        self.last_modified_timestamp = timezone.now()
        return super().save(force_insert, force_update, using, update_fields)

    # @classmethod
    # def get_fields(cls):
    #     fields = []
    #     opts = cls._meta
    #     fields.extend([f.name for f in chain(opts.concrete_fields, opts.private_fields) if f.editable])
    #     fields.extend([f.name for f in opts.many_to_many])
    #     return fields

    # def to_dict(self):
    #     opts = self._meta
    #
    #     data = {}
    #     for f in chain(opts.concrete_fields, opts.private_fields):
    #         data[f.name] = f.value_from_object(self)
    #     for f in opts.many_to_many:
    #         data[f.name] = [i.id for i in f.value_from_object(self)]
    #
    #     return data

    def to_entity(self, include_m2m_fields=True):
        # entity_class = self.entity_class()
        # filtered_data = filter_fields(self.to_dict(), entity_class.__dataclass_fields__)
        # return entity_class(**filtered_data)
        raise NotImplementedError()

    # def entity_class(self):
    #     raise NotImplementedError()

    class Meta:
        abstract = True