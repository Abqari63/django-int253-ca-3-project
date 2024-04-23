from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from .models import Note
from .forms import NoteForm


def exportAsPDF(request):
    notes = Note.objects.all()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment;'

    data = [['S.No', 'Title', 'Description']]
    i = 1
    for note in notes:
        data.append([i, note.title, Paragraph(note.description, getSampleStyleSheet()["BodyText"])])
        i += 1

    doc = SimpleDocTemplate(response, pagesize=letter)
    table = Table(data)
    style = TableStyle([('GRID', (0, 0), (-1, -1), 1, colors.black)])

    table.setStyle(style)
    doc.build([table])
    return response

def about (request):
    return render(request, "notes/about.html")

def contactus (request):
    return render(request, "notes/contactus.html")


def note_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/readNotes.html', {'notes': notes})

def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/createAndEditNote.html', {'form': form})

def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/createAndEditNote.html', {'form': form})

def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'notes/deleteNote.html', {'note': note})
