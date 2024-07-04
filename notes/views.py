from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from notes.forms import NoteForm
from notes.models import Note

# Create your views here.
class NoteListView(ListView):
    model = Note
    context_object_name = "notes"
    template_name = "notes/note_list.html"
    paginate_by = 25

class NoteDetailView(DetailView):
    model = Note
    context_object_name = "note"
    template_name = "notes/note_detail.html"

def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("note-list")
    else:
        form = NoteForm()

    context = {"form": form}

    return render(request, "notes/note_create.html", context=context)