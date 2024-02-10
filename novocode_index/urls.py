from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', auth_views.LoginView.as_view(template_name="novocode_index/login.html"), name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page="index"), name='logout'),
    path('signup', views.SignUpView.as_view(template_name="novocode_index/signup.html"), name='signup'),
    path('submit', views.SubmitSolutionView.as_view(template_name="novocode_index/submit.html"), name='submit'),
    path('submissions', views.SubmissionListView.as_view(template_name="novocode_index/submissions.html"), name='submissions'),
    path('submission/<str:token>', views.SubmissionDetailView.as_view(template_name="novocode_index/submission.html"), name='submission'),
    path('problemset', views.ProblemListView.as_view(template_name="novocode_index/problems.html"), name='problems'),
    path('problem/<int:pk>', views.ProblemDetailsView.as_view(template_name="novocode_index/problem.html"), name='problem'),
    path('create_problem', views.CreateProblemView.as_view(template_name="novocode_index/create_problem.html"), name='create_problem'),
]
