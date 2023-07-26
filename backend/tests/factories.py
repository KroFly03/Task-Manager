import factory.django
from pytest_factoryboy import register

from tasks.models import Task


@register
class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task
        skip_postgeneration_save = True

    title = factory.Sequence(lambda n: f"Title {n}")
    description = factory.Sequence(lambda n: f"Description {n}")

    completed = True

    @factory.post_generation
    def set_completed_field(self, create, extracted, **kwargs):
        if extracted is not None:
            self.completed = extracted
