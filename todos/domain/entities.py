import dataclasses
import datetime
from typing import Callable

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

    def __post_init__(self):
        if len(self.value.split(' ')) > 15:
            raise ValueError('description max 15 words')


@dataclasses.dataclass
class Todo:
    title: Title
    description: Description
    created_date: datetime.date
    _now: Callable = datetime.date.today

    def days_since_created(self):
        return (self._now() - self.created_date).days

    def dict(self):
        return {'title': self.title.value,
                'description': self.description.value,
                'daysSinceCreated': self.days_since_created()}