from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('get_sub_dir', views.get_sub_dir, name='get_sub_dir')
]
