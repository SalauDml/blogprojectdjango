from django.shortcuts import render,redirect
from .models import BlogPost,category,Comments
from .forms import Model_form,addBlogPostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_page_view(request):
    posts = BlogPost.objects.all
    return render(request,"main/index.html",{'posts': posts})

def blog_detail_page(request,blog_id):
   
    blog_post=BlogPost.objects.get(id=blog_id)
    blog_categories= category.objects.all()
    similar_posts= BlogPost.objects.all().filter(category=blog_post.category).exclude(id=blog_post.id)
    comments= Comments.objects.filter(blog_post=blog_post)
    form = Model_form()
    context = {
        "post":blog_post,
        "categories":blog_categories,
        "similar_posts":similar_posts,
        "comments":comments,
        "form":form
    } 
    if request.method == 'POST':
        form_data = Model_form(request.POST)
        if form_data.is_valid():
            form_data=form_data.save(commit=False)
            form_data.blog_post= blog_post
            form_data=form_data.save()
            return redirect('blog-detail',blog_id=blog_post.id)
        else:
            messages.error(request,"An error occured in one of your form fields")
    return render(request,"main/post.html",context)

def category_posts_page(request,category_name):
    posts = BlogPost.objects.all().filter(category__name= category_name)
    context = {
        "posts": posts
    }
    return render(request,"main/category.html",context)

@login_required
def add_blog_posts(request):
    form = addBlogPostForm()
    context = {
        'form':form
    }
    if request.method == 'POST':
        form_data = addBlogPostForm(request.POST, request.FILES)
        if form_data. is_valid():
            form_data.save(commit=False)
            form_data.owner=request.user
            form_data.save()
            return redirect('home')
    return render(request,"main/addpost.html",context)