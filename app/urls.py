from django.urls import path
from django.conf.urls.static import static 
from django.conf import settings 
from . import views
from .views import MyOrderView,notifications,order_successful,Orderview,UserRegisterView,UserEditView,ProfileView,profile_upload,AddCatagoryView,HomeView,UpdatePostView,CatagoryView,DeletePostView,ArticleDetailView,AddPostView

urlpatterns = [
    # path('', views.home, name="home"),
    path('',HomeView.as_view(), name="home"),
    path('notifications',notifications,name='notifications'),
    path('order',Orderview,name='order'),
    path('order_success',order_successful,name='order_success'),
    # path('',views.header,name='homes'),
    path('article/<int:pk>',ArticleDetailView.as_view(),name="article-details"),
    path('orders/<int:pk>',MyOrderView.as_view(),name="order-details"),
    path('add_items/',AddPostView.as_view(),name="add_post"),
    path('article/edit/<int:pk>',UpdatePostView.as_view(),name="update"),
    path('article/<int:pk>/delete',DeletePostView.as_view(),name="delete"),
    path('catagory/',AddCatagoryView.as_view(),name="catagory"),
    # path('header/<int:pk>',AddHeaderView.as_view(),name="header"),
    path('catagory/<str:cats>/',CatagoryView,name="catagoryview"),
    path('upload-csv/', profile_upload, name="profile_upload"),
    path('profile/<int:pk>',ProfileView.as_view(),name="profile"),
    path('edit_profile/',UserEditView.as_view(),name="editProfile"),
    path('register/',UserRegisterView.as_view(),name="register"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

