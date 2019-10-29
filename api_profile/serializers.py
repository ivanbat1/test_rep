from rest_framework import serializers
from .models import UserAPI


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserAPI
        fields = ('id', 'name', 'surname', 'date_create', 'date_update', 'img')

    def create(self, validate_data):
        user = UserAPI.objects.create(name=validate_data['name'],
                                      surname=validate_data['surname'],
                                      img=validate_data['img']
                                      )
        return user

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.img = validated_data.get('img', instance.img)
        instance.save()
        return instance