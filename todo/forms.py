from django import forms
from django.forms.widgets import DateTimeInput

from todo.models import Task, Tag


class TaskForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Write what to do here...",
            }
        ),
        required=True,
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
    )
    deadline = forms.DateTimeField(
        widget=DateTimeInput(
            attrs={
                "class": "datetimepicker",
                "placeholder": "DD/MM/YYYY HH:MM",
                "data-datepicker-format": "dd/mm/yyyy HH:MM",
                "type": "datetime-local",
            }
        ),
        required=False,
    )

    class Meta:
        model = Task
        fields = [
            "content",
            "deadline",
            "is_done",
            "tags",
        ]
