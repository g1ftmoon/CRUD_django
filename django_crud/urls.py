from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('applications.account.urls')),
    path('posts/', include('applications.post.urls')),
    path('comments/', include('applications.comment.urls')),
]
