import uuid

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django import forms
from django.forms import ModelForm

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
    source = forms.CharField(widget=forms.Textarea, required=False)
    source_file = forms.FileField(required=False, label="Or select a file")

    def clean(self):
        super().clean()
        if not (self.cleaned_data["source"] or self.cleaned_data["source_file"]):
            raise ValidationError("Enter source code or submit source file")


class SubmitSolutionProblemForm(forms.Form):
    compiler = forms.ModelChoiceField(Compiler.objects.all())
    source = forms.CharField(widget=forms.Textarea, required=False)
    source_file = forms.FileField(required=False, label="Or select a file")

    def clean(self):
        super().clean()
        if not (self.cleaned_data["source"] or self.cleaned_data["source_file"]):
            raise ValidationError("Enter source code or submit source file")


class CreateProblemForm(ModelForm):
    class Meta:
        model = Problem
        fields = ["name", "statement", "problem_xml", "problem_archive"]
