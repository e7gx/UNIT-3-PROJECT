from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from Product.models import Product
from .serializers import ProductSerializer
from django.contrib.auth.decorators import login_required



@login_required
@api_view(['GET'])
def api_view(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)