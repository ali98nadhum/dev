from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    data_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Book(models.Model):

    status_book = [
        ('متاح','متاح'),
        ('مستاجر' , 'مستاجر'),
        ('مباع' , 'مباع')
    ]

    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250, null=True , blank=True)
    cover = models.ImageField(upload_to='photos' , null=True , blank=True)
    pages = models.IntegerField(null=True , blank=True)
    price = models.DecimalField(max_digits=5 , decimal_places=1 , null=True , blank=True)
    retal_price_day = models.DecimalField(max_digits=5 , decimal_places=1 , null=True , blank=True)
    retal_period = models.IntegerField(null=True , blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50 , choices=status_book ,null=True , blank=True)
    category = models.ForeignKey(Category , on_delete=models.PROTECT ,null=True , blank=True)
    data_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class CustomerNew(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True , blank=True)
    address = models.CharField(max_length=250)
    mobile = models.CharField(max_length=20, default='')
    data_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    statusOrder = [
        ('تم التوصيل' , 'تم التوصيل'),
        ('جاري التوصيل' , 'جاري التوصيل')
    ]

    status = models.CharField(max_length=50 , choices=statusOrder)
    data_create = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(CustomerNew , on_delete=models.PROTECT)
    book = models.ManyToManyField(Book)

    def __str__(self):
        return self.status