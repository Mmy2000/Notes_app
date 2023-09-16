from django.shortcuts import get_object_or_404, render , redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Note , Category
from .forms import NoteForm
from django.views.generic import ListView ,DetailView
from django.db.models.query_utils import Q
from django.db.models import Count
from django.contrib import messages






class PostList(ListView):
    model = Note
    paginate_by = 4
    template_name = 'notes.html'

    def get_queryset(self) :
        user = self.request.user
        name = self.request.GET.get('q','')
        object_list = Note.objects.filter(
            user = user 
        )
        return object_list
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all().annotate(post_count=Count('post_category'))
        return context

class PostDetail(DetailView):
    model = Note
    template_name = 'notes_details.html'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all().annotate(post_count=Count('post_category'))
        context["recent_posts"] = Note.objects.all().order_by('-craeted')[:3]
        return context


def note_add(request):
    try :
        if request.method == "POST" :
            form = NoteForm(request.POST)

            if form.is_valid():
                new_form = form.save(commit=False)
                new_form.user = request.user
                new_form.save()
                messages.success(request, "Note Is Added Succssefully.")
                return redirect('/notes')

        else:
            form = NoteForm
        context = {
            'form' : form ,
        }
        
        return render(request, 'add.html' , context)
    except :
        return redirect('/accounts/login')


def edit(request , slug):
    note = get_object_or_404(Note , slug=slug)
    if request.method == "POST" :
        form = NoteForm(request.POST , instance=note)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            messages.success(request, "Note Is Updated Succssefully.")
            return redirect('/notes')

    else:
        form = NoteForm(instance=note)
    context = {
        'form' : form
    }
    


    return render(request, 'create.html' , context)

def delete_note(request , slug):
    note = get_object_or_404(Note , slug=slug)
    context = {'post': note}    
    
    if request.method == 'GET':
        return render(request, 'post_confirm_delete.html',context)
    elif request.method == 'POST':
        note.delete()
        messages.success(request,  'The post has been deleted successfully.')
        return redirect('/notes')



class PostByCategory(ListView):
    model = Note
    template_name = 'notes.html'    

    def get_queryset(self) :
        slug = self.kwargs['slug']
        object_list = Note.objects.filter(
            Q(category__name__icontains = slug)
        )
        return object_list
    
