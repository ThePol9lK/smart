from django.test import TestCase
from django.urls import reverse
from main.models import Course
from django.contrib.auth.models import User


class CourseViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.course = Course.objects.create(title="Python", anons="Изучаем Python", slug="python")

    def test_course_list_view(self):
        """Тестируем, что список курсов загружается корректно"""
        response = self.client.get(reverse("course"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/course_list.html")

    def test_course_detail_view(self):
        """Тестируем детальную страницу курса"""
        response = self.client.get(reverse("course-detail", kwargs={"slug": self.course.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Изучаем Python")

    def test_registration_vies(self):
        """Тестируем регистрацию пользователя"""
        response = self.client.post(reverse("register"),  {
            "username": "testuser",
            "password": "testpass123"
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username="testuser").exists())

    def test_login_view(self):
        """Тестируем логин"""
        user = User.object.create_user(username="testuser", password="testpass123")
        response = self.client.post(reverse("login"), {
            "username": "testuser",
            "password": "testpass123"
        })
        self.assertEqual(response.status_code, 302)






