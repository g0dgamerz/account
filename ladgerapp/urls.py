from . import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('journal/', views.journal, name = "journal"),
    path('', views.home, name = "home"),
    path('<detail>', views.journaldetails, name = "journaldetails"),
    path('add/',views.add_account,name='add'),
    path('edit/<int:id>', views.edit,name='edit'),
    path('delete/<int:id>', views.destroy,name='delete'),
]
