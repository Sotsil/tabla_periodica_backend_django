from rest_framework.viewsets import ModelViewSet
from .models import Elementos
from .serializer import ElementosSerializer

class ElementosViewSet (ModelViewSet):
    serializer_class = ElementosSerializer
    queryset = Elementos.objects.all()
    

# Create your views here.
