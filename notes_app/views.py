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

def post_details(request,id):
    user = request.user
    note=Note.objects.get(id=id,user=user)
    recent_posts = Note.objects.filter(user=user).order_by('-craeted')[:9]
    tags = Tag.objects.all()
    context = {
        'note':note,
        'recent_posts':recent_posts,
        'tags':tags
    }
    return render(request,'notes_details.html',context)

class PostByTags(ListView):
    model = Note
    template_name = 'notes_by_tags.html'
    paginate_by=3


    def get_queryset(self) :
        slug = self.kwargs['slug']
        object_list = Note.objects.filter(
            Q(tags__name__icontains = slug),
        )
        return object_list.filter(user=self.request.user)

    
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


def edit(request ,id):
    note = get_object_or_404(Note , id=id)
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

def delete_note(request , id):
    note = get_object_or_404(Note , id=id)
    context = {'post': note}    
    
    if request.method == 'GET':
        return render(request, 'post_confirm_delete.html',context)
    elif request.method == 'POST':
        note.delete()
        messages.success(request,  'The post has been deleted successfully.')
        return redirect('/notes')

    
