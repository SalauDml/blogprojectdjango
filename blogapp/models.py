from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class tag (models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class category(models.Model):
    name= models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class BlogPost(models.Model):
    title =models.CharField(max_length=200)
    description=models.TextField(null=True, blank=True)
    post = models.TextField()
    author = models.CharField(max_length=200)
    owner = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    published_date=models.DateField(auto_now_add=True)
    update_at= models.DateTimeField(auto_now=True)
    category= models.ForeignKey(category,on_delete=models.CASCADE,default=4)
    blog_image = models.ImageField(upload_to="blogs",null=True,blank=True)
    tag = models.ManyToManyField(tag)

    def __str__(self) -> str:
        return self.title

class Comments(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField()
    comment= models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    blog_post=models.ForeignKey(BlogPost,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name} comment"