from django.urls import path

from . import views

urlpatterns = [
    path('', views.Splash, name='splash'),
    path('celebrity', views.Index, name='index'),
    path('celebrity/<int:zodiac_value>', views.Individuals, name='individuals'),
    path('calculator', views.Calculator, name='calculator'),
    path('calculate', views.Calculate, name='calculate')
]