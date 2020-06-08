from rest_framework import serializers
from .models import Intent


class IntentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Intent
        fields= "__all__"