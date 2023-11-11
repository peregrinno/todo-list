# import sereliazers from the REST framework
from rest_framework import serializers
  
# import the todo data model
from .models import Todo
  
# create a sereliazer class
class TodoSerializer(serializers.ModelSerializer):
  
    # create a meta class
    class Meta:
        model = Todo
        fields = ('id', 'titulo','descricao','completa')