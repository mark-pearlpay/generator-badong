from rest_framework import serializers

from infrastructure.models import <%= namePascalCase %>Model


class <%= namePascalCase %>Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = <%= namePascalCase %>Model
        fields = '__all__'
