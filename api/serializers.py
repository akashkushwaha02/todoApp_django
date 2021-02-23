from rest_framework import serializers
from todoApp.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    create_date = serializers.ReadOnlyField()
    date_completed = serializers.ReadOnlyField()
    class Meta:        
        model = Todo
        fields = ['id','taskName','description','create_date','date_completed','important']

class TodoCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id']
        read_only_fields = ['id','taskName','description','create_date','date_completed','important']