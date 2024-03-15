from django import forms
from .models import Book , Category , CustomerNew , Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# ADD category form
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

        labels = {
            'name' : 'اضافه قسم'
        }

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'})
        }


# Add book form
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'cover',
            'pages',
            'price',
            'retal_price_day',
            'retal_period',
            'status',
            'category',
        ]

        labels = {
            'title': 'اسم الكتاب',
            'author': 'المؤلف',
            'cover': 'صوره الكتاب',
            'pages': 'عدد الصفحات',
            'price': 'السعر',
            'retal_price_day': 'سعر الإيجار في اليوم',
            'retal_period': 'فترة الإيجار',
            'status': 'حاله الكتاب',
            'category': 'التصنيف',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'author': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'cover': forms.FileInput(attrs={'class': 'form-control mt-2'}),
            'pages': forms.NumberInput(attrs={'class': 'form-control mt-2'}),
            'price': forms.NumberInput(attrs={'class': 'form-control mt-2'}),
            'retal_price_day': forms.NumberInput(attrs={'class': 'form-control mt-2'}),
            'retal_period': forms.NumberInput(attrs={'class': 'form-control mt-2'}),
            'status': forms.Select(attrs={'class': 'form-control mt-2'}),
            'category': forms.Select(attrs={'class': 'form-control mt-2'}),
        }


# Add customer form
class AddCustomerForm(forms.ModelForm):
    
    class Meta:
        model = CustomerNew
        fields = [
            'name',
            'age',
            'address',
            'mobile'
        ]

        labels = {
            'name': 'اسم الزبون',
            'age': 'العمر',
            'address': 'عنوان الزبون',
            'mobile': 'رقم الهاتف'
        }

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'age': forms.NumberInput(attrs={'class': 'form-control mt-2'}),
            'address': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control mt-2'}),
        }

# Add order form
class AddOrderForm(forms.ModelForm):
    book = forms.ModelMultipleChoiceField(queryset=Book.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'form-control mt-2'}))
    class Meta:
        model = Order
        fields = [
            'status',
            'customer',
            'book'
        ]

        labels = {
            'status': 'حاله الطلب',
            'customer': 'صاحب الطلب',
            'book': 'محتوى الطلب'
        }

        widgets = {
            'status' : forms.Select(attrs={'class': 'form-control mt-2'}),
            'customer': forms.Select(attrs={'class': 'form-control mt-2'}),
        }



# Register user form
class registerNewUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2']