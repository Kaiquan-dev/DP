"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from my_app.views import index_page
from my_app.views import current_user
from my_app.views import list_books
from my_app.views import list_users
from my_app.views import form_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
    path('current_user/<int:id>', current_user),
    path('list_books/', list_books),
    path('list_users/', list_users),
    path('form/', form_page),
]
