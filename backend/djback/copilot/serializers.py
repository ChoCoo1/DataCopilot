from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate

#推送第二次
class DatabaseConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatabaseConnection
        fields = ['username', 'sql_type', 'sql_address', 'sql_port', 'sql_login_name', 'sql_pwd', 'sql_name',
                  'created_at']


class PartialDatabaseConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatabaseConnection
        fields = ['sql_name', 'sql_type', 'sql_address', 'sql_port', 'id']


class DatabaseNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatabaseConnection
        fields = ['id', 'sql_name']
