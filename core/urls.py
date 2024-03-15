
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home , name='home' ),
    path('books/' , views.books , name='books'),
    path('books/<int:category_id>/', views.books, name='books'),
    path('add_book/' , views.addBook , name='addBook'),
    path('delete/<str:pk>',views.delete , name='delete' ),
    path('update/<str:pk>',views.update , name='update' ),
    path('customer/' , views.customer , name="customer"),
    path('add_customer/' , views.AddCustomer , name='addCustomer'),
    path('delete_customer/<str:pk>',views.deleteCustomer , name='deleteCustomer' ),
    path('update_customer/<str:pk>',views.updateCustomer , name='updateCustomer' ),
    path('orders/', views.allOrders , name='orders'),
    path('add_orders/' , views.AddOrder , name='addOrder'),
    path('delete_order/<str:pk>',views.deleteOrder , name='deleteOrder' ),
    path('update_order/<str:pk>',views.updateOrder , name='updateOrder' ),
    path('login/' , views.userLogin , name='login'),
    path('register/' , views.userRegister , name='register'),
    path('logout' , views.userLogout , name='logout'),
    
]
