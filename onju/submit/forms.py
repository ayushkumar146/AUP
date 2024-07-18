from django import forms
from submit.models import CodeSubmission

LANGUAGE_CHOICES = [
    ("py", "Python"),
    ("c", "C"),
    ("cpp", "C++"),
]


class CodeSubmissionForm(forms.ModelForm):
    language = forms.ChoiceField(choices=LANGUAGE_CHOICES)
    code = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 10000,  # Adjust the number of rows
        'cols': 10088,  # Adjust the number of columns
        'style': 'width:60vw; height:80vh;',  # Adjust width
        'placeholder': 'Write your code here...',  # Placeholder text
        'class': 'code-area'  # Additional CSS class for styling
    }))
    input_data = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 10000,  # Adjust the number of rows
        'cols': 10088,  # Adjust the number of columns
        'style': 'width:20vw; height:40vh;',  # Adjust width
        'placeholder': 'Input',  # Placeholder text
        'class': 'code-area'  # Additional CSS class for styling
    }))
    class Meta:
        model = CodeSubmission
        fields = ["language", "code", "input_data"]