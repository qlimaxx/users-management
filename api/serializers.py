from django.conf import settings
from rest_framework import serializers

from .models import User


class UserListSerializer(serializers.ListSerializer):

    email_field = 'email'
    message = 'Email address exists more than once in current list.'

    def validate(self, data):
        errors = []
        emails = set()
        for user in data:
            if user[self.email_field] in emails:
                errors.append(self.message)
            else:
                emails.add(user[self.email_field])
        if errors:
            raise serializers.ValidationError({self.email_field: errors})
        return data


class UserSerializer(serializers.ModelSerializer):

    birthday = serializers.DateField(
        format=settings.DATE_FORMAT, input_formats=[settings.DATE_FORMAT])

    class Meta:
        model = User
        list_serializer_class = UserListSerializer
        exclude = ('id',)
