from django.urls import path, include
from .views import createRecord, showRecord

urlpatterns = [
   path('show/', showRecord, name = 'show_record'),
   path('create/', createRecord, name = 'create_record'),
]
