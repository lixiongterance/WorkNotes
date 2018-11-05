from django import forms

from .models import Dir, Note

class DirForm(forms.ModelForm):
    class Meta:
        model = Dir
        fields = ['name', 'desc', 'parent_dir']
        labels = {}
