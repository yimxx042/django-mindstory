from django import forms
from .models import Page

class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title','content','feeling','score','dt_created']
    # title = forms.CharField(max_length=100, label='title')
    # content = forms.CharField(widget=forms.Textarea, label='content')
    # feeling = forms.CharField(max_length=80, label='Mind Status')
    # score = forms.IntegerField(label='Mind Scores')
    # dt_created = forms.DateField(label='Created Date')
