from django.core.mail import send_mail
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, TemplateView

from .models import Course, CourseType
from .forms import ContactForm, RegistrationForm


class UserRegisterView(CreateView):
    """
    Представление для регистрации нового пользователя.
    Отображает форму для регистрации и обрабатывает отправку данных.
    После успешной регистрации пользователя перенаправляет на страницу входа.
    """
    form_class = RegistrationForm
    template_name = "main/reg.html"
    success_url = reverse_lazy("login")


class UserLoginView(LoginView):
    """
    Представление для входа пользователя.
    Обрабатывает запросы на вход и перенаправляет на главную страницу после успешной аутентификации.
    """
    template_name = "main/log.html"

    def get_success_url(self):
        """
        Метод для получения URL после успешного входа.
        Перенаправляет пользователя на главную страницу.
        """
        return reverse_lazy("home")


class UserLogoutView(LogoutView):
    """
    Представление для выхода пользователя.
    После выхода из системы перенаправляет на страницу входа.
    """
    next_page = reverse_lazy("login")


class CourseDetailView(DetailView):
    """
    Представление для отображения подробной информации о курсе.
    Отображает данные конкретного курса, полученные через параметр 'slug' в URL.
    Включает информацию о типе курса.
    """
    model = Course
    template_name = "main/one-course.html"
    context_object_name = "course"

    def get_object(self, queryset=None):
        """
        Метод для получения курса по slug.
        Использует slug для поиска курса в базе данных.
        """
        slug = self.kwargs.get("slug")
        return get_object_or_404(Course, slug=slug)


class CourseListView(ListView):
    """
    Представление для отображения списка всех курсов.
    Фильтрует курсы по типу, используя связь с моделью CourseType.
    """
    model = Course
    template_name = "main/course.html"
    context_object_name = "courses"

    def get_queryset(self):
        """
        Метод для получения курсов по типу.
        Если параметр 'type_slug' передан в URL, фильтрует курсы по типу.
        """
        type_slug = self.kwargs.get("type_slug")
        if type_slug:
            course_type = get_object_or_404(CourseType, slug=type_slug)
            return Course.objects.filter(course_type=course_type)
        return Course.objects.all()

    def get_context_data(self, **kwargs):
        """
        Добавляет список типов курсов в контекст для отображения на странице.
        """
        context = super().get_context_data(**kwargs)
        context["course_types"] = CourseType.objects.all()
        return context


class IndexView(TemplateView):
    """
    Представление для отображения главной страницы с курсами.
    """
    template_name = "main/index.html"


class AboutView(TemplateView):
    """
    Представление для страницы 'О нас'.
    Отображает информацию о компании или организации.
    """
    template_name = "main/about.html"


class ContactsView(TemplateView):
    """
    Представление для страницы контактов.
    Отображает страницу с контактной информацией.
    """
    template_name = "main/contacts.html"


class ContactFormView(CreateView):
    """
    Представление для обработки формы обратной связи.
    При отправке формы собирает данные и отправляет их на указанный email.
    """
    form_class = ContactForm
    template_name = "main/index.html"

    def form_valid(self, form):
        """
        Метод для обработки успешной отправки формы.
        Отправляет email с данными формы на указанный адрес.
        """
        name = form.cleaned_data["name"]
        phone = form.cleaned_data["phone"]
        message = f"Имя: {name}\nТелефон: {phone}"
        send_mail(
            "Новое сообщение от пользователя",
            message,
            "ssmart.4dmin@yandex.ru",
            ["master_yoda_man@mail.ru"],
            fail_silently=False,
        )
        return super().form_valid(form)

    def get_success_url(self):
        """
        Метод для перенаправления на главную страницу после успешной отправки формы.
        """
        return reverse_lazy("home")
