from django.shortcuts import render
from django.http import HttpResponse
from my_app.models import User
from my_app.models import Book
from datetime import date

def index_page(request):
    return render(request, 'index.html')

def list_users(request):
    all_users = User.objects.all()
    return render(request, 'list_users.html', locals())

def list_books(request):
    all_books = Book.objects.all()
    return render(request, 'list_books.html', locals())

def current_user(request, id):
    current_user = User.objects.get(id=id)
    
    age = (date.today() - current_user.birthdate).days // 365
    return render(request, 'current_user.html', locals())

def form_page(request):
    return render(request, 'form.html')

# def postuser(request):
    # получаем из данных запроса POST отправленные через форму данные
    name = request.POST.get("name", "Undefined")
    age = request.POST.get("age", 1)
    return HttpResponse(f"<h2>Name: {name}  Age: {age}</h2>")