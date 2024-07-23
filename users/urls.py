from django.urls import path
from .views import signup_view,user_blog_posts
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns=[
    path('signup',signup_view,name="user-signup"),
    path('login',LoginView.as_view(template_name="accounts/login.html"),name='user-login'),
    path('logout',LogoutView.as_view(),name='user-logout'),
    path('userposts',user_blog_posts,name='user-posts')
]