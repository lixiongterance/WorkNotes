from django.shortcuts import render

from .models import Dir, Note

# Create your views here.

def index(request):
    """Home page"""
    return render(request, 'index.html')

def dirs(request, dir_id=None):
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
