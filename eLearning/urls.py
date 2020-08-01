#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('index/', views.index, name='blog-index'),
    path('blog/', views.blog, name='blog-blog'),
    path('contact/', views.contact, name='blog-contact'),
    path('instructors/', views.instructors, name='blog-instructors'),
    path('courses/', views.courses, name='blog-courses'),
    path('single-course/', views.single_course, name='blog-single_course'),

    
]
