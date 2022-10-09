from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Note


def home(request): 
    if request.user.is_staff:
        context = {
            'notes': Note.objects.all()
        }
        return render(request, 'notes/doctor_view.html', context)
    else:
        for note in Note.objects.all():
            if note.author == request.user:
                context = {
                    'notes': note
                }
        return render(request, 'notes/home.html', context)


class NoteListView(ListView):
    model = Note
    template_name = 'notes/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'notes'
    ordering = ['-date_posted']
    


class NoteDetailView(DetailView):
    model = Note


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['name', 'recepta']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Note
    fields = ['name', "author",'recepty', "lekarstwa", "badania"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class NoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Note
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'notes/about.html', {'name': 'About'})


def portal(request):
    return render(request, 'notes/portal.html', {'name': 'Portal'})


def form(request):
    return render(request, 'notes/form.html', {'name': 'Portal'})

