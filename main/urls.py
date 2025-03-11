from django.urls import path
from .views import (
    IndexView,
    AboutView,
    ContactsView,
    CourseListView,
    CourseDetailView,
    ContactFormView,
    UserLoginView,
    UserLogoutView,
    UserRegisterView,
)

urlpatterns = [
    # Главная страница
    path('', IndexView.as_view(), name='home'),

    # Страница "О нас"
    path('about/', AboutView.as_view(), name='about'),

    # Страница "Контакты"
    path('contacts/', ContactsView.as_view(), name='contacts'),

    # Список всех курсов (с возможностью фильтрации по типу)
    path('courses/', CourseListView.as_view(), name='course'),
    path('courses/<slug:type_slug>/', CourseListView.as_view(), name='course-list-filtered'),

    # Детальная информация о курсе
    path('course/<slug:slug>/', CourseDetailView.as_view(), name='course-detail'),

    # Форма обратной связи
    path('send_message/', ContactFormView.as_view(), name='send_message'),

    # Аутентификация
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
]
