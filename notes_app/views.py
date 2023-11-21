from django.shortcuts import get_object_or_404, render , redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Note 
from .forms import NoteForm
from django.views.generic import ListView ,DetailView
from django.db.models.query_utils import Q
from django.db.models import Count
from django.contrib import messages
from django.core.paginator import Paginator
from taggit.models import Tag




def notelist(request):
    user = request.user
    my_notes = Note.objects.filter(user=user).order_by('-craeted')
    paginator = Paginator(my_notes, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'notes.html',{
        'user' : user ,
        'page_obj' : page_obj
    })

class PostDetail(DetailView):
    model = Note
    template_name = 'notes_details.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context["recent_posts"] = Note.objects.filter(user=user).order_by('-craeted')[:3]
        context["tags"] = Tag.objects.all()
        return context





def note_add(request):
        if request.method == "POST" :
            form = NoteForm(request.POST,request.FILES)

            if form.is_valid():
                new_form = form.save(commit=False)
                new_form.user = request.user
                new_form.save()
                form.save_m2m()
                messages.success(request, "Note Is Added Succssefully.")
                return redirect('/notes')

        else:
            form = NoteForm
        context = {
            'form' : form ,
        }
        
        return render(request, 'add.html' , context)


def edit(request , slug):
    note = get_object_or_404(Note , slug=slug)
    if request.method == "POST" :
        form = NoteForm(request.POST , instance=note)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            form.save_m2m()
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

    
