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
    image = models.ImageField(upload_to='books/',verbose_name="download image")
    title = models.CharField(max_length=100, verbose_name="book title")
    description = models.TextField(verbose_name="book description", blank=True)
    price = models.PositiveIntegerField(verbose_name="book price", default=10)
    created_dat = models.DateField(auto_now_add=True)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES,default='HORROR', verbose_name="book genre")
    gmail = models.URLField(verbose_name="book gmail", blank=True,default='esenbektima@gmail.com')
    author = models.CharField(max_length=50, verbose_name="book author",default='Timur Tumur')
    audio = models.URLField(verbose_name="url book",blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'



