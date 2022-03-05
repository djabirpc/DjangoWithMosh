from django.shortcuts import render
from django.db import connection
from store.models import Collection, Order, OrderItem, Product

def say_hello(request):
    with connection.cursor() as cursor:
        cursor.callproc('get_customers',[1, 2, 'a'])
    return render(request,'hello.html',{'name':'Djabir', 'result': list(queryset)})