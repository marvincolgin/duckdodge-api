from django.urls import path
from . import views

urlpatterns = [
    path('races/', views.RaceList.as_view()),
    path('races/<int:pk>/', views.RaceDetail.as_view()),
    path('boats/', views.BoatList.as_view()),
    path('boats/<int:pk>/', views.BoatDetail.as_view()),
]
