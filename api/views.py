from datetime import datetime

from django.conf import settings
from rest_framework import exceptions, mixins, status, viewsets
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


class UserViewSet(
        mixins.CreateModelMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset_filters = {'from': 'birthday__gte',
                        'to': 'birthday__lte'}
    error_message = 'It must be in DD.MM.YYYY format'

    def get_queryset(self):
        queryset = User.objects.all()
        queryset = self.apply_filters(queryset)
        return queryset

    def apply_filters(self, queryset):
        filters = {}
        for field in self.queryset_filters:
            value = self.request.query_params.get(field, None)
            if value:
                try:
                    dt = datetime.strptime(value, settings.DATE_FORMAT)
                except ValueError:
                    raise exceptions.ValidationError(
                        dict([(field, self.error_message)]))
                filters[self.queryset_filters[field]] = dt
        if filters:
            queryset = queryset.filter(**filters)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers)
