from django import forms
from .models import Comments,BlogPost

class Model_form(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name','email','comment']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'comment':forms.Textarea(attrs={'class':'form-control'})
        }



class addBlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title','description','post','author','category','blog_image','tag']