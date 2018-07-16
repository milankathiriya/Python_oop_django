from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


def home(request):
    return render(request, 'index.html')

def class_page(request):
    return render(request, 'oop_app/class.html')

class Encapsulation(TemplateView):
	template_name = 'oop_app/encap_abstract.html'

# def encapsulation(request):
#     return render(request, 'oop_app/encap_abstract.html')

def inheritance(request):
    return render(request, 'oop_app/inheritance.html')

def multilevel(request):
    return render(request, 'oop_app/multilevel_inheritance.html')

def multiple(request):
    return render(request, 'oop_app/multiple_inheritance.html')

def method_overloading(request):
    return render(request, 'oop_app/method_overloading.html')

def method_overriding(request):
    return render(request, 'oop_app/method_overriding.html')

def polymorphism(request):
    return render(request, 'oop_app/polymorphism.html')
