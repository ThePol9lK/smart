from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import CourseListView, CourseDetailView, UserRegisterView


class UrlsTest(SimpleTestCase):
    def test_course_list_url_resolves(self):
        """Проверяем, что урл списка курсов корректно привязан"""
        url = reverse("course")
        self.assertEqual(resolve(url).func.view_class, CourseListView)

    def test_course_detail_url_resolves(self):
        """Проверяем, что урл детального курса корректно привязан"""
        url = reverse("course-detail", kwargs={"slug": "python"})
        self.assertEqual(resolve(url).func.view_class, CourseDetailView)

    def test_register_url_resolves(self):
        """Проверяем, что урл регистрации работает"""
        url = reverse("register")
        self.assertEqual(resolve(url).func.view_class, UserRegisterView)
