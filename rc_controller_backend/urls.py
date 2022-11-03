from django.urls import path

from . import views

urlpatterns = [
  path('getData', views.getData, name='getData'),
  path('writeData', views.writeData, name='writeData'),
  path('writeStatus', views.writeStatus, name='writeStatus'),
  path('updateStatus', views.updateStatus, name='updateStatus'),

]