from rest_framework.serializers import ModelSerializer
from .models import Elementos

class ElementosSerializer (ModelSerializer):
    class Meta:
        model = Elementos
        fields = '__all__'