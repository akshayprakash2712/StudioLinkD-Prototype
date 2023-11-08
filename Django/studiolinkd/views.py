from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from .forms import RegistrationForm,EditProfileForm
from .models import Artist,Client,RadioChannel,TvChannel
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account was created  ")
            return redirect('signin')  # Replace 'home' with your desired redirect URL
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.TYPE_CHOICES == 'A':
            login(request, user)
            return redirect('artist')  
        elif  user is not None and user.TYPE_CHOICES == 'B':
            login(request, user)
            return redirect('client')
        elif  user is not None and user.TYPE_CHOICES == 'C':
            login(request, user)
            return redirect('tv')
        elif user is not None and user.TYPE_CHOICES == 'D':
            login(request, user)
            return redirect('radio')
        else:
                print("Invalid Credentials")
           
    return render(request, 'signin.html')

def home(request):
    return render(request,'home.html',{})
def LogoutUser(request):
    logout(request)
    return redirect('signin')

@login_required()
def artist(request):
    artist_view = Artist.objects.all()
    return render(request,'artist.html',{'artist_view': artist_view})

@login_required()
def client(request):
    client_view = Client.objects.all()
    return render(request,'client.html',{'client_view': client_view})

@login_required()
def tv(request):
    return render(request,'tv.html',{})

@login_required()
def radio(request):
    return render(request,'radio.html',{})

@login_required()
def EditView(request):
    user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('signin')  # Redirect to the user's profile page
    else:
        form = EditProfileForm(instance=user)
    return render(request, 'edit.html', {'form': form})

def change_password(request):
    user = request.user  # Get the user object

    if user.has_usable_password():
        if request.method == 'POST':
            password_form = PasswordChangeForm(user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)  # Update the session to prevent logout
                messages.success(request, 'Your password was successfully changed.')
                return redirect('signin')  # Redirect to the profile page
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            password_form = PasswordChangeForm(user)

        return render(request, 'password_change.html', {'password_form': password_form})

    else:
        messages.warning(request, 'You cannot change your password because no password is set. Contact an administrator.')
        return redirect('signin') 


def atrist_list(request):
    atrist_list = Artist.objects.all()
    p = Paginator(Artist.objects.all(),3)
    page = request.GET.get('page')
    venues = p.get_page(page)
   
    return render(request,'artist_list.html',{'artist_list' : atrist_list,'venues': venues})





def client_list(request):
    client_list = Client.objects.all()
    p = Paginator(Client.objects.all(),3)
    page = request.GET.get('page')
    venues = p.get_page(page)
   
    return render(request,'client_list.html',{'client_list' : client_list,'venues': venues})





def tv_list(request):
    tv_list = TvChannel.objects.all()
    p = Paginator(TvChannel.objects.all(),3)
    page = request.GET.get('page')
    venues = p.get_page(page)
   
    return render(request,'tv_list.html',{'tv_list' : tv_list,'venues': venues})



def radio_list(request):
    radio_list = RadioChannel.objects.all()
    p = Paginator(RadioChannel.objects.all(),3)
    page = request.GET.get('page')
    venues = p.get_page(page)
   
    return render(request,'radio_list.html',{'radio_list' : radio_list,'venues': venues})