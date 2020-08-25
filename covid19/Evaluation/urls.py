from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('question/', question, name='question'),
    path('list1/', view_list1, name='list1'),
    path('list2/', view_list2, name='list2'),
    path('list3/', view_list3, name='list3'),
    path('result/', result, name='result'),


]
