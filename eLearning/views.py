
from django.shortcuts import render

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]

context = {
        'posts': posts
    }

def home(request):
    return render(request, 'blog/home.html', context)

def index(request):
    return render(request, 'blog/index.html')

def blog(request):
    return render(request, 'blog/blog.html')    

def courses(request):
    return render(request, 'blog/courses.html') 

def single_course(request):
    return render(request, 'blog/single-course.html')  

def instructors(request):
    return render(request, 'blog/instructors.html')    

def contact(request):
    return render(request, 'blog/contact.html')             