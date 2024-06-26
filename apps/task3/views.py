from django.http import JsonResponse
from django.shortcuts import render

from apps.task3.models import Product


def view_function(request):
    products = Product.objects.all()
    serialized_products = [products.get_encrypted_fields() for product in products]
    return JsonResponse({'products': serialized_products})
