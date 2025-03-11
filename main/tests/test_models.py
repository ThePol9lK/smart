from django.test import TestCase
from main.models import Course
from django.utils.text import slugify


class CourseModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(title="Тестовый курс", anons="Описание курса")

    def test_course_creation(self):
        """Проверяем, что курс создается правильно"""
        self.assertEqual(self.course.title, "Тестовый курс")
        self.assertEqual(self.course.anons, "Описание курса")

    def test_course_slug(self):
        """Проверяем, что slug генерируется автоматически"""
        self.assertEqual(self.course.slug, slugify("Тестовый курс"))

    def test_get_absolute_url(self):
        """Проверяем, что метод get_absolute_url работает правильно"""
        self.assertEqual(self.course.get_absolute_url(), f"/course/{self.course.slug}/")


