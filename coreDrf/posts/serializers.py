from rest_framework import serializers
from .models import Posts


class SerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = (
            'title',
            'post_id',
            'category',
            'start_date',
            'change_date'
        )
