from rest_framework import viewsets
from .models import User, DataScienceModel, Subscription
from .serializers import UserSerializer, DataScienceModelSerializer, SubscriptionSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DataScienceModelViewSet(viewsets.ModelViewSet):
    queryset = DataScienceModel.objects.all()
    serializer_class = DataScienceModelSerializer

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
