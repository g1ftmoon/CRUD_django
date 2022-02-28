from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from applications.comment.models import Comment
from applications.comment.permission import IsCommenterAuthorized
from applications.comment.serializers import CommentSerializer


class CommentListView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsCommenterAuthorized,]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, ]