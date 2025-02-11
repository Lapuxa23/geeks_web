from django.db import models


class BookModel(models.Model):
    GENRE_CHOICES = (
        ('HORROR', 'Ужасы'),
        ('FANTASY', 'Фэнтези'),
        ('ROMANCE', 'Роман'),
        ('SCI-FI', 'Научная фантастика'),
        ('THRILLER', 'Триллер'),
        ('MYSTERY', 'Детектив'),
        ('NON-FICTION', 'Нон-фикшн'),
        ('HISTORICAL', 'Историческая проза'),
        ('ADVENTURE', 'Приключения'),
        ('BIOGRAPHY', 'Биография'),
        ('DYSTOPIAN', 'Антиутопия'),
        ('POETRY', 'Поэзия'),
        ('SELF-HELP', 'Саморазвитие'),
        ('PHILOSOPHY', 'Философия'),
        ('CHILDREN', 'Детская литература'),
        ('YOUNG-ADULT', 'Подростковая литература'),
        ('COMICS', 'Комиксы и графические романы'),
        ('DRAMA', 'Драма'),
        ('CRIME', 'Криминальная литература'),
        ('CLASSIC', 'Классическая литература'),
    )

    image = models.ImageField(upload_to='books/', verbose_name="Обложка книги")
    title = models.CharField(max_length=100, verbose_name="Название книги")
    description = models.TextField(verbose_name="Описание книги", blank=True)
    price = models.PositiveIntegerField(verbose_name="Цена", default=10)
    created_date = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES, verbose_name="Жанр книги")
    email = models.EmailField(verbose_name="Email автора", blank=True, default='esenbektima@gmail.com')
    author = models.CharField(max_length=50, verbose_name="Автор", default='Timur Tumur')
    audio_url = models.URLField(verbose_name="Ссылка на аудиокнигу", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Review(models.Model):
    STARS = (
        ("🌟", "🌟"),
        ("🌟🌟", "🌟🌟"),
        ("🌟🌟🌟", "🌟🌟🌟"),
        ("🌟🌟🌟🌟", "🌟🌟🌟🌟"),
        ("🌟🌟🌟🌟🌟", "🌟🌟🌟🌟🌟"),
    )
    choice_books = models.ForeignKey(BookModel, on_delete=models.CASCADE,
                                    related_name='books')
    created_at = models.DateField(auto_now_add=True)
    review_text = models.TextField(default='крутая книга')
    stars = models.CharField(max_length=10, choices=STARS, default='🌟🌟')

    def __str__(self):
        return f'{self.stars}-{self.choice_books.title}'
