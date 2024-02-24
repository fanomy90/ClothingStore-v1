from django.urls import path, re_path
from . import views
from .views import *

urlpatterns = [
    #Статические маршруты
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    #Динамические маршруты
    #path('storeItem/', views.storeItem, name='storeItem'),
    #path('storeCat/', views.storeCat, name='storeCat'),
    path('storeItem/<slug:storeItem_slug>/', storeItem.as_view(), name='storeItem'),
    path('storeCat/<slug:storeCat_slug>/', storeCat.as_view(), name='storeCat'),
]