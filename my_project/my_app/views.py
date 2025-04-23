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

def current_user_age(request, id):
    current_user = User.objects.get(id=id)
    
    age = (date.today() - current_user.birthdate).days // 365
    return render(request, 'current_user.html', locals())

def form_page(request):
    return render(request, 'form.html')

def current_user(request):
    if request.method == 'POST':
        user_current_email = request.POST.get("user_current_email")
        user_current_password = request.POST.get("user_current_password")
        
        try:
            user = User.objects.get(user_email=user_current_email)
            if user.user_password == user_current_password:
                return HttpResponse(f"<h2>Name: {user.user_name} Surname: {user.user_surname}</h2>")
            else:
                return HttpResponse('Неправильно: неверный пароль')
            
        except User.DoesNotExist:
            return HttpResponse('Неправильно: пользователь не найден')
        
    return HttpResponse('Метод не поддерживается. Используйте POST.')
    