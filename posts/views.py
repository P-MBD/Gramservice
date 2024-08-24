from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from django.http import JsonResponse

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

def post_count(request):
    count = Post.objects.count()
    return JsonResponse({'count': count})