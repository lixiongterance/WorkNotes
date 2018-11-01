from itertools import chain

from django.shortcuts import render

from .models import Dir, Note

# Create your views here.

def index(request):
    """Home page"""
    return render(request, 'index.html')

def notes(request, dir_id=None):
    """list all dirs and files in root"""
    # 实际是相同的，可以合并为第一个去掉if判断
    if dir_id == None or dir_id.strip() == '':
        dirs = Dir.objects.filter(parent_dir=None)
        notes = Note.objects.filter(parent_dir=None)
        items = list(chain(dirs, notes))
    else:
        dir_obj = Dir.objects.get(id=dir_id)
        dirs = dir_obj.dir_set.all()
        notes = dir_obj.note_set.all()
        items = list(chain(dirs, notes))

    context = {'items': items}
    return render(request, 'work_notes/notes.html', context)
