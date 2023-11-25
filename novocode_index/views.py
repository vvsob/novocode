import uuid

import django.shortcuts
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import CreationForm, SubmitSolutionForm, SubmitSolutionProblemForm
from submissions.models import Submission
from problems.models import Problem
from format_verdict import format_verdict


def index(request):
    return render(request, "novocode_index/index.html")


class SignUpView(generic.CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("login")
    template_name = "novocode_index/signup.html"


class SubmitSolutionView(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        f = SubmitSolutionForm()
        return render(request, "novocode_index/submit.html", {'form': f})

    def post(self, request, *args, **kwargs):
        f = SubmitSolutionForm(request.POST)
        f.is_valid()

        submission = Submission()
        submission.token = str(uuid.uuid4())
        submission.owner = request.user
        submission.problem = f.cleaned_data['problem']
        submission.compiler = f.cleaned_data['compiler']
        submission.source = request.FILES['source']

        submission.save()
        submission.send_testing()

        return django.shortcuts.redirect(reverse_lazy("submissions"))


class SubmissionListView(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        submissions = []
        for submission in self.request.user.submissions.all().order_by('-timestamp'):
            submissions.append({
                'token': submission.token,
                'timestamp': submission.timestamp,
                'problem': submission.problem,
                # 'verdict': submission.verdict,
                'verdict': format_verdict(submission.verdict),
                'compiler': submission.compiler
            })
        return render(request, self.template_name, {'submissions': submissions})


class SubmissionDetailView(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        submission = get_object_or_404(Submission, token=self.kwargs['token'])
        with submission.source.open('r') as source_file:
            source = source_file.read()
        return render(request, self.template_name, {'submission': submission, 'source': source})


class ProblemListView(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        problems = Problem.objects.order_by('-id')
        return render(request, self.template_name, {'problems': problems})


class ProblemDetailsView(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        problem = get_object_or_404(Problem, pk=self.kwargs['pk'])
        blocks = problem.statement['blocks']
        form = SubmitSolutionProblemForm()
        return render(request, self.template_name, {'problem': problem, 'blocks': blocks, 'form': form})

    def post(self, request, *args, **kwargs):
        problem = get_object_or_404(Problem, pk=self.kwargs['pk'])

        f = SubmitSolutionProblemForm(request.POST)
        f.is_valid()

        submission = Submission()
        submission.token = str(uuid.uuid4())
        submission.owner = request.user
        submission.problem = problem
        submission.compiler = f.cleaned_data['compiler']
        submission.source = request.FILES['source']

        submission.save()
        submission.send_testing()

        return django.shortcuts.redirect(reverse_lazy("submissions"))
