from django import forms
from .models import Post, Catagories,Profile,order
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm,UserCreationForm, UserChangeForm


choices = Catagories.objects.all().values_list('name','name')

class OrderForm(forms.ModelForm):
    class Meta:
        model = order
        fields = '__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','stock','image','image2','image3','image4','image5','image6','catagory' ,'body','price')
        widgets = {
            "title" : forms.TextInput(attrs={"class":"form-control","placeholder":"Name of the Product"}), 
            "catagory" : forms.Select(choices=choices,attrs={"class":"form-control"}), 
            "body" : forms.Textarea(attrs={"class":"form-control"}), 
        }
        labels = {
        "body": "Description",
        "image":"Image of Your Product ( Image 1)",
        "image2":"Image of Your Product ( Image 2)",
        "image3":"Image of Your Product ( Image 3)",
        "image4":"Image of Your Product ( Image 4)",
        "image5":"Image of Your Product ( Image 5)",
        "image6":"Image of Your Product ( Image 6)",
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','stock','image','image2','image3','image4','image5','image6','catagory' ,'body','price')
        widgets = {
            "title" : forms.TextInput(attrs={"class":"form-control","placeholder":"Name of the Product"}), 
            "catagory" : forms.Select(choices=choices,attrs={"class":"form-control"}), 
            "body" : forms.Textarea(attrs={"class":"form-control"}), 
        }
        labels = {
        "body": "Description",
        "image":"Image of Your Product ( Image 1)",
        "image2":"Image of Your Product ( Image 2)",
        "image3":"Image of Your Product ( Image 3)",
        "image4":"Image of Your Product ( Image 4)",
        "image5":"Image of Your Product ( Image 5)",
        "image6":"Image of Your Product ( Image 6)",
        }

class UserEditForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}) )
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    website_url = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    facebook_url = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    twitter_url = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    linkdin_url = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    bio = forms.CharField(max_length=100,widget=forms.Textarea(attrs={"class":"form-control"}))

    
    class Meta:
        model = Profile
        fields = ('first_name','last_name','username','email','image','address','mobile_no','bio','website_url','facebook_url','twitter_url','linkdin_url')

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}) )
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))

    
    class Meta:
        model = Profile
        fields = ('first_name','last_name','username','email','password','image','address','mobile_no','bio','website_url','facebook_url','twitter_url','linkdin_url')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__( *args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
class Orders(forms.ModelForm):
    class Meta:
        model = order
        fields = [
            'product_id',
            'customer_id',
            'is_approved',
            'address',
            'quantity'
        ]
        widgets = {
            "address" : forms.Textarea(attrs={"class":"form-control"}), 
        }
