from faker import Faker

from todos.domain.entities import Todo, Title


class TodoBuilder:
    def __init__(self):
        faker = Faker()
        self._object = Todo(title=Title(value=faker.sentence(nb_words=4)),
                            description=faker.sentence(),
                            days_since_created=faker.pyint(min_value=0))

    def build(self):
        return self._object