from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    message = models.TextField()  # متن پست
    created_time = models.DateTimeField(auto_now_add=True)  # زمان ایجاد پست
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)  # تصویر پست (اختیاری)
    likes_count = models.PositiveIntegerField(default=0)  # تعداد لایک‌ها
    comments_count = models.PositiveIntegerField(default=0)  # تعداد نظرات
    shares_count = models.PositiveIntegerField(default=0)  # تعداد اشتراک‌گذاری‌ها

    def __str__(self):
        return f"Post by {self.user.username} at {self.created_time}"
