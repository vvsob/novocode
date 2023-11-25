from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProblemList.as_view()),
    path('<int:pk>', views.ProblemDetail.as_view()),
]
