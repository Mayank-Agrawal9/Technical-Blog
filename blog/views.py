from django.db.models.fields.files import ImageField
from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Category, Contact, Post

# Create your views here.

def home(request):
    #Load all the post from database(10)
    posts = Post.objects.all()[:11]
    date = Category.objects.all()
    data = {
        'posts': posts,
        'date':date
    }
    return render(request, 'home.html', data)

def contact(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        phone = request.POST['phone']
        email = request.POST['email']
        country = request.POST['state']
        subject = request.POST['subject']
        contact = Contact(name=firstname, phone =phone,email=email,state = country, subject = subject)
        contact.save()

    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def post(request,url):
    post = Post.objects.get(url=url)
    date = Category.objects.all()
    return render(request,'posts.html',{'post':post,'date':date})
