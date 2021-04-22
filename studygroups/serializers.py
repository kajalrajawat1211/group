from rest_framework import serializers
from .models import userLogin,userRegister

class userLoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=userLogin
        fields='__all__'
class userRegisterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=userRegister
        fields='__all__'

