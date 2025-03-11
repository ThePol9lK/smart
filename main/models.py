from django.db import models
from django.utils.text import slugify


class CourseType(models.Model):
    """
    Модель, представляющая вид курса.

    Атрибуты:
    ----------
    name : str
        Название типа курса (например, "Обычный курс", "Повышение квалификации", "Профессиональная переподготовка").
    slug : str
        Уникальное короткое имя для URL, автоматически создается из названия.
    description : str (опционально)
        Описание категории курсов, может быть пустым.
    """

    name = models.CharField(
        'Название',
        max_length=100,
        unique=True,
        db_index=True,
        help_text="Введите название вида курса (например, 'Повышение квалификации')."
    )
    slug = models.SlugField(
        'URL',
        unique=True,
        blank=True,
        help_text="Автоматически создается из названия."
    )
    description = models.TextField(
        'Описание',
        blank=True,
        null=True,
        help_text="Дополнительная информация о виде курса (необязательно)."
    )

    class Meta:
        verbose_name = 'Вид курса'
        verbose_name_plural = 'Виды курсов'
        ordering = ['name']

    def save(self, *args, **kwargs):
        """
        Переопределенный метод сохранения:
        - Генерирует slug на основе name, если он не задан.
        """
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        """Возвращает строковое представление объекта (название вида курса)."""
        return self.name


class Course(models.Model):
    """
    Модель, представляющая учебный курс.

    Атрибуты:
    ----------
    title : str
        Название курса.
    slug : str
        Уникальное короткое имя для URL, создается автоматически из названия.
    course_type : ForeignKey (CourseType)
        Связь с моделью `CourseType`, указывающая на тип курса.
    anons : str
        Краткое описание курса (анонс).
    text : str
        Полное описание курса.
    created_at : datetime
        Дата и время создания записи (автоматически).
    updated_at : datetime
        Дата и время последнего обновления записи (автоматически).
    is_active : bool
        Флаг активности курса (по умолчанию `True`).
    """

    title = models.CharField(
        'Название курса',
        max_length=100,
        db_index=True,
        help_text="Введите название курса (например, 'Основы программирования')."
    )
    slug = models.SlugField(
        'URL',
        unique=True,
        blank=True,
        help_text="Автоматически создается из названия."
    )
    course_type = models.ForeignKey(
        CourseType,
        on_delete=models.PROTECT,
        related_name='courses',
        verbose_name='Вид курса',
        help_text="Выберите категорию курса."
    )
    anons = models.TextField(
        'Краткое описание',
        help_text="Короткое описание курса, которое будет отображаться в списке."
    )
    text = models.TextField(
        'Полное описание',
        help_text="Полное описание курса с программой обучения."
    )
    created_at = models.DateTimeField(
        'Дата создания',
        auto_now_add=True,
        help_text="Автоматически устанавливается при создании."
    )
    updated_at = models.DateTimeField(
        'Дата обновления',
        auto_now=True,
        help_text="Автоматически обновляется при изменении записи."
    )
    is_active = models.BooleanField(
        'Активен',
        default=True,
        db_index=True,
        help_text="Определяет, отображается ли курс на сайте."
    )

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['-created_at']
        unique_together = ('title', 'course_type')

    def save(self, *args, **kwargs):
        """
        Переопределенный метод сохранения:
        - Генерирует slug на основе title, если он не задан.
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        """Возвращает строковое представление объекта (название курса + его категория)."""
        return f"{self.title} ({self.course_type.name})"
