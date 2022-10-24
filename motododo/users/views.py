from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegisterForm, ContactForm
from accomodation.models import Accomodation
from .models import Favorite
from django.core.mail import send_mail


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            messages.success(request, f'Un compte pour {username} a été créé!')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')


@login_required
def save(request):
    if request.method == "POST":
        current_user = request.user
        accomodation = request.POST.get('elt_id')
        accomodation_saved = Accomodation.objects.get(
                                        auto_increment_id=accomodation
                                        )
        Favorite.objects.get_or_create(
            user=current_user,
            accomodation_saved=accomodation_saved
            )

    return redirect('home')


@login_required
def fav(request):
    current_user = request.user
    favs = Favorite.objects.filter(user=current_user)
    accomodations_favs = [fav.accomodation_saved for fav in favs]
    contexte = {'accomodations_favs': accomodations_favs}

    return render(request, 'users/fav.html', contexte)


@login_required
def delete_fav(request):
    if request.method == "POST":
        current_user = request.user
        elt = request.POST.get('fav_id')
        fav = Accomodation.objects.get(auto_increment_id=elt)
        fav_delete = Favorite.objects.filter(
                                user=current_user,
                                accomodation_saved=fav
                                )
        fav_delete.delete()
    return redirect('users:fav')


@login_required
def delete_account(request):
    if request.method == "POST":
        if not request.user.is_superuser:
            current_user = request.user
            user = User.objects.get(username=current_user.username)
            user.delete()
    return redirect('home')


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            content = form.cleaned_data['content']
            msg_mail = str(content) + " -- " + str(contact_email)
            send_mail(
                contact_name,
                msg_mail,
                contact_email,
                ['openriderfr@gmail.com'],
            )
            messages.success(request, 'Votre message a été envoyé. Merci !')
            return redirect('home')
    else:
        form = ContactForm()

    return redirect('home')
