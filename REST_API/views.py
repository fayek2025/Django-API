from django.shortcuts import render
from .models import Post
from .serializer import PostSerializers
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
# Create your views here.

def PostsView(request):
    if request.method == 'GET':
        posts = Post.objects.all() #queryset
        serializer = PostSerializers(posts , many = True)
        return JsonResponse(serializer.data , safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer  = PostSerializers(data= data)
        
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data , status = 201)
        
        return JsonResponse(serializer.data , status = 400)
