from django.contrib.auth.models import Group, User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


# PK 로 Hyperlinked 를 사용하지 않고 PK 또는 다양한 관계를 사용해도 되지만
# Hyperlinking is good RESTful design 이라고 설명하고 있다.