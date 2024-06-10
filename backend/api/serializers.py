from rest_framework import serializers
from .models import User, DataScienceModel, Subscription

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_subscribed']

class DataScienceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataScienceModel
        fields = '__all__'

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
