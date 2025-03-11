# 📌 Умней – образовательная платформа

## 📝 Описание  
**Умней** – это веб-приложение на Django, предоставляющее образовательные курсы.  
Проект использует **PostgreSQL** и **Docker** для удобного развертывания.  

---

## 🚀 Технологии  

- 🐍 **Python 3.11**  
- 🌍 **Django**  
- 🗄 **PostgreSQL**  
- 📦 **Docker + Docker Compose**

---

## 📥 Установка и запуск  

### 1️⃣ Клонирование репозитория  
```sh
git clone https://github.com/ThePol9lK/ymnei.git
cd ymnei
```
### 2️⃣ Создание .env файла
Скопируйте env.template и заполните данными:
```sh
cp env.template .env
```
Пример .env:
```env
ALLOWED_HOSTS=127.0.0.1,localhost
SECRET_KEY=секретный_ключ
DEBUG=True
POSTGRES_DB=dbname
POSTGRES_USER=user
POSTGRES_PASSWORD=password
DB_HOST=db
DB_PORT=5432
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_USE_SSL=False
EMAIL_HOST_USER=email@example.com
EMAIL_HOST_PASSWORD=пароль
```
### 3️⃣ Запуск проекта с Docker
```sh
docker-compose up --build -d
```
Проект запустится на http://127.0.0.1:8000/

### 4️⃣ Применение миграций и создание суперпользователя
```sh
docker-compose exec django_app python manage.py migrate
docker-compose exec django_app python manage.py createsuperuser
```
Проект запустится на http://127.0.0.1:8000/

---

## 📂 Структура проекта
```plaintext
/app
│── main/                   # Основное Django-приложение
│   ├── models.py           # Модели БД
│   ├── views.py            # Контроллеры
│   ├── urls.py             # Маршруты
│   ├── templates/          # HTML-шаблоны
│   ├── static/             # CSS, JS, изображения
│
│── config/                 # Конфигурация проекта
│── requirements.txt        # Python-зависимости
│── Dockerfile              # Docker-образ для Django
│── docker-compose.yml      # Docker Compose конфигурация
│── manage.py               # Основной скрипт Django
│── README.md               # Документация проекта
```
---

## 📞 Контакты
#### 📧 Email: laa2610@gmail.com
#### 📌 Telegram: @Bjorn3228