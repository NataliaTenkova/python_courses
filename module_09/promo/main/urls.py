from django.urls import path, include
from . import views

urlpatterns = [
    path('index', views.index, name = 'Index'),
    path('reg', views.reg, name = 'Reg'),
    path('user', views.user, name = 'User'),

]
