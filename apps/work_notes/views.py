from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Dir, Note
from .forms import DirForm, NoteForm

# Create your views here.

def index(request):
    """Home page"""
    return render(request, 'index.html')

def dir(request, dir_id=None):
    """list all dirs and files in root"""
    if dir_id == None or dir_id == '0':
        dir_id = 0
        real_dir = None
    else:
        real_dir = dir_id

    dirs = Dir.objects.filter(parent_dir=real_dir).order_by('date_added')
    notes = Note.objects.filter(parent_dir=real_dir).order_by('date_added')
    
    context = {'dirs': dirs, 'notes': notes, 'cur_dir_id': dir_id}
    return render(request, 'work_notes/dir.html', context)

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

def new_note(request, dir_id=None):
    """add a new note"""
    if dir_id != None and dir_id != '0':
        cur_dir = Dir.objects.get(id=dir_id)
    else:
        cur_dir = None
        dir_id = 0

    if request.method != 'POST':
        item_form = NoteForm()
    else:
        item_form = NoteForm(data=request.POST)
        if item_form.is_valid():
            new_item = item_form.save(commit=False)
            new_item.parent_dir = cur_dir
            new_item.save()
            return HttpResponseRedirect(reverse('work_notes:items:dir', 
                                                args=[dir_id]))

    context = {'item_form': item_form, 'cur_dir_id': dir_id}
    return render(request, 'work_notes/new_note.html', context)

def edit_note(request, note_id):
    """edit a note"""
    note = Note.objects.get(id=note_id)

    if request.method != 'POST':
        note_form = NoteForm(instance=note)
    else:
        note_form = NoteForm(instance=note, data=request.POST)
        if note_form.is_valid():
            note_form.save()
            return HttpResponseRedirect(reverse('work_notes:items:note',
                                               args=[note.id]))

    context = {'note_form': note_form, 'note': note}
    return render(request, 'work_notes/edit_note.html', context)
