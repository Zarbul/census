from django.contrib.auth import forms
from django.contrib.auth import get_user_model
from django import forms
from django.utils.translation import gettext_lazy as _

from census.models import People, Language, Department


class PeopleCreationForm(forms.ModelForm):
    class Meta:
        model = People
        fields = ('f_name', 'l_name', 'age', 'gender', 'department', 'language',)


class LanguageCreationForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ('name',)


class DepartmentCreationForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('name', 'floor')


