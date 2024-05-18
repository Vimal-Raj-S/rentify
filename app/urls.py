from django.urls import path
from . import views

urlpatterns = [
    path('', views.house_list),
    path('Add/', views.AddHouse),
    path('Edit/<id>', views.EditHouse),
    path('Delete/<eid>', views.DeleteHouse),
    path('View/<eid>', views.ViewHouse),
    path('login/', views.Login)
]