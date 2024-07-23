from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from blogapp.models import BlogPost

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form_data=UserRegistrationForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('home')
    
    form = UserRegistrationForm()
    context = {
        "form":form
    }
    return render(request, "accounts/signup.html", context)

def user_blog_posts(request):
    blogpost = BlogPost.objects.all()
    user_blog_post= blogpost.filter(owner = request.user)
    context = {
        'posts': user_blog_post
    }
    return render(request,"main/userblogposts.html",context)