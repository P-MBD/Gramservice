from django.urls import path
from .views import PostViewSet, post_count
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('posts/count/', post_count, name='post_count'),  # مسیر جدید
]

urlpatterns += router.urls  # اضافه کردن مسیرهای router