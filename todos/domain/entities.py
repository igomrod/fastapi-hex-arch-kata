import dataclasses

from pydantic import BaseModel, validator


@dataclasses.dataclass
class Title:
    value: str

    def __post_init__(self):
        if len(self.value.split(' ')) > 5:
            raise ValueError('title max five words')


@dataclasses.dataclass
class Description:
    value: str


@dataclasses.dataclass
class Todo:
    title: Title
    description: Description
    days_since_created: int

    def dict(self):
        return {'title': self.title.value,
                'description': self.description.value,
                'daysSinceCreated': self.days_since_created}