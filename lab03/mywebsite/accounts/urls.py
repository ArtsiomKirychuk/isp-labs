from .import views
from django.urls import path, include


urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),

    path('', views.home, name="home"),
    path('user/', views.userPage, name='user-page'),
    path('products/', views.products, name="products"),
    path('customer/<str:primary_key>/', views.customer, name="customer"),

    path('create_order/<str:primary_key>/', views.createOrder, name='create_order'),
    path('update_order/<str:primary_key>/', views.updateOrder, name='update_order'),
    path('delete_order/<str:primary_key>/', views.delete_order, name='delete_order')
]