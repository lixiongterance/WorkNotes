from django import forms

from .models import Dir, Note

class DirForm(forms.ModelForm):
    class Meta:
        model = Dir
        '''
        这里parent_dir先直接选择
        后续改成选择列表默认值为当前目录
        '''
        fields = ['name', 'desc', 'parent_dir']
        labels = {'name': 'dir name', 'desc': 'dir desc', 'parent_dir': 'parent dir'}
