from rest_framework import generics
from .serializer import PizzaSerializer
from .models import Pizza
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated

class PizzaList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class PizzaDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer



