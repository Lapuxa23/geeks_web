# Generated by Django 5.1.5 on 2025-02-05 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='books/', verbose_name='download image')),
                ('title', models.CharField(max_length=100, verbose_name='book title')),
                ('description', models.TextField(blank=True, verbose_name='book description')),
                ('price', models.PositiveIntegerField(default=10, verbose_name='book price')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('genre', models.CharField(choices=[('HORROR', 'Ужасы'), ('FANTASY', 'Фэнтези'), ('ROMANCE', 'Роман'), ('SCI-FI', 'Научная фантастика'), ('THRILLER', 'Триллер'), ('MYSTERY', 'Детектив'), ('NON-FICTION', 'Нон-фикшн'), ('HISTORICAL', 'Историческая проза'), ('ADVENTURE', 'Приключения'), ('BIOGRAPHY', 'Биография'), ('DYSTOPIAN', 'Антиутопия'), ('POETRY', 'Поэзия'), ('SELF-HELP', 'Саморазвитие'), ('PHILOSOPHY', 'Философия'), ('CHILDREN', 'Детская литература'), ('YOUNG-ADULT', 'Подростковая литература'), ('COMICS', 'Комиксы и графические романы'), ('DRAMA', 'Драма'), ('CRIME', 'Криминальная литература'), ('CLASSIC', 'Классическая литература')], default='HORROR', max_length=20, verbose_name='book genre')),
                ('gmail', models.URLField(blank=True, default='esenbektima@gmail.com', verbose_name='book gmail')),
                ('author', models.CharField(default='Timur Tumur', max_length=50, verbose_name='book author')),
                ('audio', models.URLField(blank=True, verbose_name='url book')),
            ],
        ),
    ]
