from django.contrib import admin
from django.urls import path
from . import views

app_name = 'appOne'

urlpatterns = [
    path('', views.home, name='home_link'),
    path('mobiles/', views.mobile, name='mobile_link'),
    path('mobile_detail/<int:id>/', views.mobile_detail, name='mobile_detail_link'),
    path('pcs/', views.pc,name='pc_link'),
    path('tablets/', views.tablet, name='tablet_link'),
    path('accessories/', views.accessory, name='accessory_link'),
    path('feedback/', views.feedback, name='feedback_link'),
    path('add_product/', views.add_product, name='add_product'),
    path('update_product/<int:id>/', views.update_product, name='update_product_link'),
    path('delete_product/<int:id>/', views.delete_product, name='delete_product_link'),

]
