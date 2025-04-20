from django.contrib import admin
from my_app.models import User
from my_app.models import Book

admin.site.register(User)
admin.site.register(Book)