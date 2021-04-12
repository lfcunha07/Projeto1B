from django.shortcuts import render, redirect
from .models import Note

def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        newNote = Note(title = title, content = content)
        newNote.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def deleteNote(request, note_id):
    note_to_delete = Note.objects.get(id = note_id)
    note_to_delete.delete()
    all_notes = Note.objects.all()
    return redirect('index')
    
def editNote(request, note_id):
    if request.method == 'POST':
        note_to_save = Note.objects.get(id = note_id)
        note_to_save.title = request.POST.get('titulo')
        note_to_save.content = request.POST.get('detalhes')
        note_to_save.save()
        return redirect('index')
    else:
        note_to_edit = Note.objects.get(id = note_id)
        return render(request, 'notes/edit.html', {'note_to_edit': note_to_edit})
    