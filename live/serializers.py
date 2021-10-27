from .models import Liveimg
from rest_framework import serializers


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(use_url=True)
    def create(self, validated_data):
        return Liveimg.objects.create(**validated_data)

    class Meta:
        model = Liveimg
        fields = ('deviceUser', 'deviceId', 'image')