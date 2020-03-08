from rest_framework import generics
from .models import Visitor
from .serializer import createVisitorSerializer, UpdateVisitorSerializer, viewVisitorSerializer

class VisitorView(generics.ListAPIView):
    serializer_class = viewVisitorSerializer
    queryset = Visitor.objects.all()

class VisitorCreate(generics.CreateAPIView):
    serializer_class = createVisitorSerializer
    queryset = Visitor.objects.all()

class VisitorUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = UpdateVisitorSerializer

    def get_queryset(self):
        query = self.kwargs['pk']
        return Visitor.objects.filter(pk=query)

