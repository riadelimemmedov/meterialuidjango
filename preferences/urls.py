from django.urls import path
from .views import MyPreference

app_name = 'ustunluk'

urlpatterns = [
    path('add/', MyPreference.as_view(),name='home')
]