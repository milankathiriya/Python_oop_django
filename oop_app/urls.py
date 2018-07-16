from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('class_page/', views.class_page, name='class_page'),

    path('encapsulation/', views.Encapsulation.as_view(), name='encapsulation'),
    
    # path('encapsulation/', views.encapsulation, name='encapsulation'),
    path('inheritance/', views.inheritance, name='inheritance'),
    path('multilevel/', views.multilevel, name='multilevel'),
    path('multiple/', views.multiple, name='multiple'),
    path('method_overloading/', views.method_overloading, name='method_overloading'),
    path('method_overriding/', views.method_overriding, name='method_overriding'),
    path('polymorphism/', views.polymorphism, name='polymorphism'),
]
