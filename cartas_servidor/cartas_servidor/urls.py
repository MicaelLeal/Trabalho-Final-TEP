
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import (obtain_jwt_token,
                                      refresh_jwt_token)

from playpif import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/login/', obtain_jwt_token),
    path('user/refresh-token/', refresh_jwt_token),
    path('user/novo-usuario/', views.JogadorView.as_view()),
    path('cartas/', views.CartaList.as_view(), name=views.CartaList.name),
    path('cartas-detail/<int:pk>/', views.CartaDetail.as_view(), name=views.CartaDetail.name),
    path('sequencias/', views.SequenciaView.as_view()),
]
