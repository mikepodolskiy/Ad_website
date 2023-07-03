from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from ads.filters import AdFilter
from ads.models import Ad, Comment
from ads.permissions import IsAuthor
from ads.serializers import AdSerializer, AdDetailSerializer, CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter

    def get_serializer_class(self):
        if self.action == "retrieve" or self.action == "create":
            return AdDetailSerializer
        return AdSerializer

    @action(detail=False, methods=['get'])
    def me(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)

    def get_queryset(self):
        if self.action == 'me':
            return Ad.objects.filter(author=self.request.user).all()
        return Ad.objects.all()

    def get_permissions(self):
        if self.action in ["create", "retrieve"]:
            self.permission_classes = [IsAuthenticated]
        elif self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes = [IsAuthor, IsAdminUser]
        else:
            self.permission_classes = [AllowAny]
        return super().get_permissions()



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = AdPagination

    def get_permissions(self):
        if self.action in ["create", "retrieve"]:
            self.permission_classes = [IsAuthenticated]
        elif self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes = [IsAuthor, IsAdminUser]
        else:
            self.permission_classes = [AllowAny]

        super().get_permissions()
