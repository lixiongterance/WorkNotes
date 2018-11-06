from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Dir, Note
from .forms import DirForm

# Create your views here.

def index(request):
    """Home page"""
    return render(request, 'index.html')

def dir(request, dir_id=None):
    """list all dirs and files in root"""
    dirs = Dir.objects.filter(parent_dir=dir_id).order_by('date_added')
    notes = Note.objects.filter(parent_dir=dir_id).order_by('date_added')

    context = {'dirs': dirs, 'notes': notes}
    return render(request, 'work_notes/notes.html', context)

def note(request, note_id=None):
    """show single note's content"""
    note = Note.objects.get(id=note_id)

    context = {'note': note}
    return render(request, 'work_notes/note.html', context)

# 后面将dir和note合并
def new_dir(request):
    """add a new dir"""
    if request.method != 'POST':
        # go to new_dir page
        item_form = DirForm()
    else:
        # create a dir
        item_form = DirForm(request.POST)
        if item_form.is_valid():
            item_form.save()
            return HttpResponseRedirect(reverse('work_notes:items:dir'))

    context = {'item_form': item_form}
    return render(request, 'work_notes/new_item.html', context)
