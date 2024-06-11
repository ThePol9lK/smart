# Generated by Django 4.2.7 on 2023-11-17 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_preschool'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('anons', models.TextField(verbose_name='Анонс')),
                ('text', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Профессиональная переподготовка',
                'verbose_name_plural': 'Профессиональная переподготовка',
            },
        ),
    ]