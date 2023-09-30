from django.shortcuts import render , redirect , get_object_or_404
from .forms import SignupForm , UserForm , ProfileForm
from .models import Profile ,NewsLitter , Info
from notes_app.models import Note
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login 
from django.contrib import messages
from django.http import JsonResponse




def home(request):
    try:
        user = request.user
        recent_notes = Note.objects.filter(user=user).order_by('-craeted')[:3]

        return render(request, 'home.html',{
            'user' : user ,
            'recent_notes' : recent_notes,
        })
    except:
        return render(request, 'home.html',{})
            


def signup(request):
    if request.method == "POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            try :
                usernames = form.cleaned_data['username']
                passwords = form.changed_data["password1"]
                user = authenticate(username=usernames,password=passwords)
                login(request,user)

                return redirect('/accounts/login')
            except:
                return redirect('/accounts/login')

            
    else:
        form=SignupForm()

    return render(request,'registration/signup.html',{'form':form})



def profile(request ):
    profile = Profile.objects.get(user=request.user)

    return render(request,'profile/users-profile.html',{'profile':profile})


def edit_profile(requset):
    profile = Profile.objects.get(user=requset.user)
    if requset.method == "POST":
        user_form = UserForm(requset.POST , instance=requset.user)
        profile_form = ProfileForm(requset.POST,requset.FILES,instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            myprofile = profile_form.save(commit=False)
            myprofile.user = requset.user
            myprofile.save()
            messages.success(requset, "Profile Is Updated Succssefully.")
            return redirect('/')
    else:
        user_form = UserForm(instance=requset.user)
        profile_form = ProfileForm(instance=profile)

    return render(requset,'profile/profile_edit.html',{
        'user_form':user_form,
        'profile_form':profile_form
    })


def news_letters_subscribe(request):
    email = request.POST.get('emailinput')
    NewsLitter.objects.create(email=email)
    return JsonResponse({'done':'done'})


