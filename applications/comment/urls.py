from django.urls import path

from applications.comment.views import CommentListView

urlpatterns = [

    path('comments-list/', CommentListView.as_view())
]