from django.db import models
from django.core.validators import EmailValidator

class User(models.Model):
    user_name = models.CharField(max_length=100, blank=False)
    user_surname = models.CharField(max_length=100, blank=False)
    user_date_of_birth = models.DateField(null=True, blank=True)
    user_email = models.EmailField(
        max_length=255,
        unique=True,
        validators=[EmailValidator()],
    )
    user_password = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.user_surname} {self.user_name}'
    

class Book(models.Model):
    book_title = models.CharField(max_length=100, blank=False)
    book_pages = models.IntegerField(default=0)

    def __str__(self):
        return self.book_title