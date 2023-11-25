import uuid

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from problems.models import Problem
from compilers.models import Compiler


User = get_user_model()


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class SubmitSolutionForm(forms.Form):
    problem = forms.ModelChoiceField(Problem.objects.all())
    compiler = forms.ModelChoiceField(Compiler.objects.all())
    source = forms.FileField()


class SubmitSolutionProblemForm(forms.Form):
    compiler = forms.ModelChoiceField(Compiler.objects.all())
    source = forms.FileField()
