from django.urls import path
from . import views

urlpatterns = [
    path('tutorials', views.findall),
    path('tutorials/<int:id>', views.id_stuff),
    # path('tutorials/some-endpoint?key=value&key2=value2')
]

