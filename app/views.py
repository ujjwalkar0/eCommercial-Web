from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView
from .models import Post,Catagories,Profile,order
from .forms import PostForm, EditForm, UserEditForm,SignUpForm,Orders,OrderForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
import csv, io
from django.contrib import messages
# def home(request):
#     return render(request,'home.html',{})
class ProfileView(DetailView):
    model = Profile
    template_name = "profile.html"

def profile_upload(request):   
    template = "profile_upload.html"
    data = Post.objects.all()
    prompt = {
        'order': 'Order of the CSV should be name, email, address,    phone, profile',
        'profiles': data    
              }
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Post.objects.update_or_create(
            title=column[0],
            image=column[1],
            image2=column[2],
            image3=column[3],
            image4=column[4],
            image5=column[5],
            image6=column[6],
            stock=column[7],
            body=column[8],
            post_date=column[9],
            catagory=column[10],
            price=column[11],
        )
    context = {}
    return render(request, template, context)


class HomeView(ListView):
    model = Post
    template_name = "home.html"
    cats = Catagories.objects.all()
    ordering = ['-id']

    def get_context_data(self,*args, **kwargs):
        cat_menu = Catagories.objects.all()
        context = super(HomeView,self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def notifications(request):
    context = {
        'Posts': order.objects.all(),
    }
    return render(request,'myy_posts.html',context)

class MyOrderView(UpdateView):
    model = order
    form_class = OrderForm
    template_name = "order_details.html"

class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_details.html"

class AddCatagoryView(CreateView):
    model = Catagories
    template_name = "cat.html"  
    fields = "__all__"  

def CatagoryView(request,cats):
    catagory_posts = Post.objects.filter(catagory=cats)
    return render(request,'catagories.html',{'cats':cats.title(), 'catagory_posts':catagory_posts })

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"

# class AddHeaderView(UpdateView):
#     model = layout
#     form_class = HeaderForm
#     template_name = "HeaderImage.html"

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "update.html"

class DeletePostView(DeleteView):
    model = Post
    template_name = "delete.html"
    success_url = reverse_lazy('home')

class UserEditView(UpdateView):
    form_class = UserEditForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('editProfile')

    def get_object(self):
        return self.request.user

class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

def Orderview(request):
    form = Orders(request.POST,request.FILES)
    if form.is_valid():
        print(form)
        form.save()
        form = Orders()
    context = {
        'form': form,
    }
    system = request.POST.get('system',None)
    context['system'] = system
    return render(request,'order.html',context)

def order_successful(request):
    return render(request,'order_recieved.html',{})
    