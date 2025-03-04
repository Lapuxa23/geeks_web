# Generated by Django 5.1.5 on 2025-02-11 10:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='books/', verbose_name='Обложка книги')),
                ('title', models.CharField(max_length=100, verbose_name='Название книги')),
                ('description', models.TextField(blank=True, verbose_name='Описание книги')),
                ('price', models.PositiveIntegerField(default=10, verbose_name='Цена')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('genre', models.CharField(choices=[('HORROR', 'Ужасы'), ('FANTASY', 'Фэнтези'), ('ROMANCE', 'Роман'), ('SCI-FI', 'Научная фантастика'), ('THRILLER', 'Триллер'), ('MYSTERY', 'Детектив'), ('NON-FICTION', 'Нон-фикшн'), ('HISTORICAL', 'Историческая проза'), ('ADVENTURE', 'Приключения'), ('BIOGRAPHY', 'Биография'), ('DYSTOPIAN', 'Антиутопия'), ('POETRY', 'Поэзия'), ('SELF-HELP', 'Саморазвитие'), ('PHILOSOPHY', 'Философия'), ('CHILDREN', 'Детская литература'), ('YOUNG-ADULT', 'Подростковая литература'), ('COMICS', 'Комиксы и графические романы'), ('DRAMA', 'Драма'), ('CRIME', 'Криминальная литература'), ('CLASSIC', 'Классическая литература')], max_length=20, verbose_name='Жанр книги')),
                ('email', models.EmailField(blank=True, default='esenbektima@gmail.com', max_length=254, verbose_name='Email автора')),
                ('author', models.CharField(default='Timur Tumur', max_length=50, verbose_name='Автор')),
                ('audio_url', models.URLField(blank=True, verbose_name='Ссылка на аудиокнигу')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('review_text', models.TextField(default='крутая книга')),
                ('stars', models.CharField(choices=[('🌟', '🌟'), ('🌟🌟', '🌟🌟'), ('🌟🌟🌟', '🌟🌟🌟'), ('🌟🌟🌟🌟', '🌟🌟🌟🌟'), ('🌟🌟🌟🌟🌟', '🌟🌟🌟🌟🌟')], default='🌟🌟', max_length=10)),
                ('choice_show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shows', to='books.bookmodel')),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
