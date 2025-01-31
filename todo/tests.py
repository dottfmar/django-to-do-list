from django.test import TestCase
from django.urls import reverse

from todo.models import Task, Tag


class HomePageViewTests(TestCase):

    def setUp(self):
        tag1 = Tag.objects.create(name="home")
        tag2 = Tag.objects.create(name="work")

        self.task1 = Task.objects.create(content="Test Task 1", is_done=False)
        self.task2 = Task.objects.create(content="Test Task 2", is_done=False)

        self.task1.tags.add(tag1)
        self.task2.tags.add(tag2)

        self.url = reverse("todo:index")

    def test_mark_task_as_done(self):
        self.assertFalse(self.task1.is_done)

        response = self.client.post(
            self.url,
            {
                "task_id": self.task1.id,
                "mark_as_completed": "complete",
            },
        )

        self.task1.refresh_from_db()

        self.assertTrue(self.task1.is_done)
        self.assertRedirects(response, self.url)

    def test_mark_task_as_undone(self):
        self.task1.is_done = True
        self.task1.save()

        self.assertTrue(self.task1.is_done)

        response = self.client.post(
            self.url,
            {
                "task_id": self.task1.id,
                "mark_as_completed": "undo",
            },
        )

        self.task1.refresh_from_db()

        self.assertFalse(self.task1.is_done)
        self.assertRedirects(response, self.url)
