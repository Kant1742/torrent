from rest_framework import serializers
# from .models import HuiModel


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = HuiModel
        fields = ['id', 'title', 'slug']
