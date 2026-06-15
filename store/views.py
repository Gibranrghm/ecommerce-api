from rest_framework import viewsets, generics, permissions
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from .serializers_auth import RegisterSerializer
from .permissions import IsOwnerOrReadOnly


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    filterset_fields = ['category', 'available']
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'created_at', 'name']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RegisterView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer