from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from rest_framework.serializers import ModelSerializer
from .models import Note

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
