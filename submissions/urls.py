from django.urls import path
from . import views

urlpatterns = [
    path('', views.SubmissionList.as_view()),
    path('<str:pk>', views.SubmissionDetail.as_view()),
]
