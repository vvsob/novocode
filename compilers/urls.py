from django.urls import path
from . import views

urlpatterns = [
    path('', views.CompilerList.as_view()),
    path('<int:pk>', views.CompilerDetail.as_view()),
]
