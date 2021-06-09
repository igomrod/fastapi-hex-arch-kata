from pydantic import BaseModel, validator


class Todo(BaseModel):
    title: str
    description: str
    days_since_created: int

    @validator('title')
    def title_is_max_5_words(cls, value):
        if len(value.split(' ')) > 5:
            raise ValueError('max five words')
        return value
