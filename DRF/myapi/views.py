from rest_framework import viewsets
from .serializers import HeroSerializer
from .models import Hero

#ModelViewSet is a special view that Django Rest Framework provides. It will handle GET and POST for Heroes without us having to do any more work.
class HeroViewSet(viewsets.ModelViewSet):
    #Query the database for all heroes
    queryset = Hero.objects.all().order_by('name')

    #Pass that database queryset into the serializer we just created, so that it gets converted into JSON and rendered
    serializer_class = HeroSerializer