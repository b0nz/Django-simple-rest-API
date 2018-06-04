from rest_framework import serializers

from .models import News

# Serializers define the API representation.
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'content', 'created_at' )