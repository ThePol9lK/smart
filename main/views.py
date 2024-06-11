from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import Course, PreSchool, ExtraClass
from django.views.generic import DetailView
from django.http import HttpResponseRedirect
from .forms import ContactForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
           # email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, password=password)
            return redirect('login')  # 
    else:
        form = RegistrationForm()
    return render(request, 'main/reg.html', {'form': form})


def logout_view(request: HttpRequest):
    logout(request)
    return redirect(reverse("login"))

def login_view(request: HttpRequest):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("home")
        else:
            return render(request,"main/log.html" )
        
    username = request.POST["username"]
    password = request.POST["password"]
    
    user = authenticate(request, username = username, password = password)
    if user is not None:
        login(request, user)
        return redirect("home")
    return render(request,"main/log.html" , {"error" : "Invalid login credetionals"})
        

# # Отправка письма
# def submit_form(request):
#     if request.method == 'POST':
#         name = request.POST.get('name', '')
#         phone = request.POST.get('phone', '')
#
#         # Отправка письма
#         send_mail(
#             'Новая заявка',
#             f'Имя: {name}\nНомер телефона: {phone}',
#             'ваш_email@gmail.com',
#             ['получатель@gmail.com'],
#             fail_silently=False,
#         )
#
#         return HttpResponseRedirect('')  # Перенаправление на страницу успешной отправки
#     else:
#         return render(request, "main/index.html")


# class CourseDetailView(DetailView):
#     model = Course
#     template_name ='main/one-course.html'
#     context_object_name = 'desk'

#     def get_object(self):
#         title = self.kwargs.get('title')
#         return get_object_or_404(Course, title=title)
@login_required
def course_detail_view(request, title):
    course = get_object_or_404(Course, title=title)
    context = {'desk': course}
    return render(request, 'main/one-course.html', context)

# class PreSchoolDetailView(DetailView):
#     model = PreSchool
#     template_name ='main/one-course.html'
#     context_object_name = 'desk'

#     def get_object(self):
#         title = self.kwargs.get('title')
#         return get_object_or_404(PreSchool, title=title)
@login_required
def pre_school_detail_view(request, title):
    pre_school = get_object_or_404(PreSchool, title=title)
    context = {'desk': pre_school}
    return render(request, 'main/one-course.html', context)

# class ExtraClasslDetailView(DetailView):
#     model = ExtraClass
#     template_name ='main/one-course.html'
#     context_object_name = 'desk'

#     def get_object(self):
#         title = self.kwargs.get('title')
#         return get_object_or_404(ExtraClass, title=title)
@login_required
def extra_class_detail_view(request, title):
    extra_class = get_object_or_404(ExtraClass, title=title)
    context = {'desk': extra_class}
    return render(request, 'main/one-course.html', context)

def index(request):
    return render(request, "main/index.html")


def course(request):
    courses = Course.objects.all()
    preSchool = PreSchool.objects.all()
    extraClass = ExtraClass.objects.all()

    # Cоединение бд для последующей передачи на страницу
    context = {
        'courses': courses,
        'preSchool': preSchool,
        'extraClass': extraClass,
    }
    return render(request, "main/course.html", context)




def about(request):
    return render(request, "main/about.html")

def contatcs(request):
    return render(request, "main/contacts.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            message = 'Имя: {}\nТелефон: {}'.format(name, phone)
            send_mail(
                'Новое сообщение от пользователя',
                message,
                'ssmart.4dmin@yandex.ru', # Адрес отправителя
                ['master_yoda_man@mail.ru'], # Адрес получателя
                #пороль : max214zet
                fail_silently=False,
            )
            return render(request, 'main/index.html')
    else:
        form = ContactForm()
    return render(request, 'main/index.html', {'form': form})

