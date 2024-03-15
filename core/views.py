from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .forms import BookForm , CategoryForm , AddCustomerForm , AddOrderForm , registerNewUser
from django.contrib.auth import authenticate , logout , login
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    data_books = Book.objects.filter(active=True).order_by('-data_create')[:10]
    all_book = Book.objects.all()
    book_count = all_book.count()
    data_category = Category.objects.all()
    customer_data = CustomerNew.objects.all()
    customer_count =  customer_data.count()
    order = Order.objects.all()
    order_count = order.count()
    done_order_count = order.filter(status = 'تم التوصيل').count()
    dlever_order_count = order.filter(status = 'جاري التوصيل').count()
    if request.method == 'POST':
         add_category = CategoryForm(request.POST)
         if add_category.is_valid():
              add_category.save()
              return redirect('/')
    context = {
        'data_books': data_books,
        'data_category': data_category,
        'categoty_form' : CategoryForm,
        'customer_count': customer_count,
        'book_count':book_count,
        'order_count': order_count,
        'done_order_count': done_order_count,
        'dlever_order_count':dlever_order_count
    }
    return render(request , 'home.html' , context)


@login_required(login_url='login')
def books(request, category_id=None):
    if category_id is not None:
        category = get_object_or_404(Category, id=category_id)
        data_books = category.book_set.all()
    else:
        data_books = Book.objects.all()
    
    data_category = Category.objects.all()
    context = {
        'data_books': data_books,
        'data_category': data_category
    }
    return render(request , 'books.html' , context)

@login_required(login_url='login')
def addBook(request):
     bookForm = BookForm()
     if request.method == 'POST':
          bookForm = BookForm(request.POST , request.FILES)
          if bookForm.is_valid():
               bookForm.save()
               return redirect('/')
     context = {
          'form': BookForm()
     }
     return render(request , 'add_book.html' , context)

@login_required(login_url='login')
def delete(request, pk):
     book = Book.objects.get(id=pk)
     if request.method == 'POST':
          book.delete()
          return redirect('/')
     context = {'book': book}
     return render(request , 'delete.html' , context)


@login_required(login_url='login')
def update(request, pk):
     book = Book.objects.get(id=pk)
     form = BookForm(instance=book)
     if request.method == 'POST':
          form = BookForm(request.POST ,request.FILES ,  instance=book)
          if form.is_valid():
               form.save()
               return redirect('/')
     context = {"form": form}
     return render(request , 'edit.html' , context)

@login_required(login_url='login')
def customer(request):
     customer_data = CustomerNew.objects.all()
     return render(request , 'customer.html' , {'customer_data': customer_data})

@login_required(login_url='login')
def AddCustomer(request):
    customerForm = AddCustomerForm()
    if request.method == 'POST':
        customerForm = AddCustomerForm(request.POST)
        if customerForm.is_valid():
            customerForm.save()
            return redirect('addOrder')  
    context = {'customerForm': customerForm}
    return render(request, 'add_customer.html', context) 

@login_required(login_url='login')    
def deleteCustomer(request , pk):
     customer = CustomerNew.objects.get(id=pk)
     if request.method == 'POST':
          customer.delete()
          return redirect('customer')
     context = {'customer': customer}
     return render(request , 'delete_customer.html', context)

@login_required(login_url='login')
def updateCustomer(request , pk):
     customer = CustomerNew.objects.get(id=pk)
     form = AddCustomerForm(instance=customer)
     if request.method == 'POST':
          form = AddCustomerForm(request.POST , instance=customer)
          if form.is_valid():
               form.save()
               return redirect('customer')
     context = {'form': form}
     return render(request , 'update_customer.html', context)
     

@login_required(login_url='login')
def allOrders(request ):
  order_type = request.GET.get('type')
  if order_type == 'all':
    order_data = Order.objects.all()
  elif order_type == 'delivered':
    order_data = Order.objects.filter(status='تم التوصيل')
  elif order_type == 'in_delivery':
    order_data = Order.objects.filter(status='جاري التوصيل')
  else:
    order_data = Order.objects.all()
  context = {
    'order_data': order_data,
    'selected_type': order_type,
  }
  return render(request, 'orders.html', context)



@login_required(login_url='login')
def AddOrder(request):
     form = AddOrderForm()
     if request.method == 'POST':
          form = AddOrderForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('orders')
     context = {'form': form}
     return render(request , 'order_form.html' , context)

@login_required(login_url='login')
def deleteOrder(request , pk):
     order = Order.objects.get(id=pk)
     if request.method == 'POST':
          order.delete()
          return redirect('orders')
     context = {'order': order}
     return render(request , 'delete_order.html', context)

@login_required(login_url='login')
def updateOrder(request , pk):
     order = Order.objects.get(id=pk)
     form = AddOrderForm(instance=order)
     if request.method == 'POST':
          form = AddOrderForm(request.POST , instance=order)
          if form.is_valid():
               form.save()
               return redirect('orders')
     context = {'form': form}
     return render(request , 'update_order.html', context)


@login_required(login_url='login')
def userRegister(request):
    form = registerNewUser()
    if request.method == 'POST':
        form = registerNewUser(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request , user + 'اضافه الادمن بنجاح')
            return redirect('home')
    context= {'form': form}
    return render(request , 'register.html', context)



def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request , username=username , password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request , "Wrong username or password")
    context = {}
    return render(request , 'login.html', context)


def userLogout(request):
    logout(request)
    return redirect('login')
