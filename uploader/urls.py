from django.urls import path

from .views import index

app_name = 'uploader'

urlpatterns = [
    path('', index, name='index')
]
