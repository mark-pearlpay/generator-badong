from abc import ABC, abstractmethod

from domain import <%= namePascalCase %>


class <%= namePascalCase %>Repository(ABC):
    @abstractmethod
    def get_by_id(self, <%= nameSnakeCase %>_id) -> <%= namePascalCase %>:
        raise NotImplementedError()

    @abstractmethod
    def save(self, <%= nameSnakeCase %>: <%= namePascalCase %>) -> <%= namePascalCase %>:
        raise NotImplementedError()

    @abstractmethod
    def update(self, <%= nameSnakeCase %>: <%= namePascalCase %>) -> <%= namePascalCase %>:
        raise NotImplementedError()
