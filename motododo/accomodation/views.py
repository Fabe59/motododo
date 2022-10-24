from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Accomodation, AddAccomodation, Comment
from .forms import AddAccomodationForm, CommentForm
from decimal import Decimal
import requests
import json
import urllib
from math import acos, cos, sin, radians
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.contrib import messages


@login_required
def add(request):
    if request.method == "POST":
        form = AddAccomodationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddAccomodationForm()

    return render(request, 'accomodation/add.html', {'form': form})


def search(request):
    research = request.GET['search']
    research = research.title()
    all_result = Accomodation.objects.all()

    if not research:
        return render(
            request,
            'accomodation/all_result.html',
            {'all_result': all_result}
            )

    url = "https://nominatim.openstreetmap.org/search/<query>?"
    params = {
        "city": research,
        "format": 'json',
        }
    req = requests.get(url, params)
    data = req.json()
    lat = round(Decimal(data[0]['lat']), 6)
    lon = round(Decimal(data[0]['lon']), 6)
    final_result = []
    for elt in all_result:
        dist = 6371 * acos(
            cos(radians(Decimal(lat))) * cos(
                radians(Decimal(elt.lat))) * cos(
                    radians(Decimal(elt.lon)) - radians(
                        Decimal(lon))) + sin(
                            radians(Decimal(lat))) * sin(
                                radians(Decimal(elt.lat))))
        if dist <= 10:
            final_result.append(elt)

    if not final_result:
        return render(request, 'accomodation/noresult.html')

    else:
        return render(request,'accomodation/search.html',{'research': research, 'final_result': final_result,})


@login_required
def details(request, id):
    accomodation = Accomodation.objects.get(auto_increment_id=id)

    all_result = Accomodation.objects.all()
    others_result = []
    for elt in all_result:
        dist = 6371 * acos(
            cos(radians(Decimal(accomodation.lat))) * cos(
                radians(Decimal(elt.lat))) * cos(
                    radians(Decimal(elt.lon)) - radians(
                        Decimal(accomodation.lon))) + sin(
                            radians(Decimal(accomodation.lat))) * sin(
                                radians(Decimal(elt.lat))))
        if dist <= 10:
            others_result.append(elt)

    is_liked = False
    if accomodation.likes.filter(id=request.user.id).exists():
        is_liked = True
    comments = Comment.objects.filter(accomodation=accomodation)
    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():

            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())

            if result['success']:
                text = request.POST.get('text')
                comment = Comment.objects.create(
                                            accomodation=accomodation,
                                            user=request.user,
                                            text=text
                                            )
                comment.save()
                messages.success(
                    request, 'Votre commentaire a été ajouté. Merci!'
                    )
                return HttpResponseRedirect(accomodation.get_absolute_url())
            else:
                messages.warning(
                    request,
                    'reCAPTCHA invalide. Merci de réessayer.'
                    )
        else:
            comment_form = CommentForm()

    return render(request, 'accomodation/details.html', {
        'accomodation': accomodation,
        'is_liked': is_liked,
        'total_likes': accomodation.total_likes(),
        'comments': comments,
        'comment_form': comment_form,
        'others_result': others_result
        })


@login_required
def like(request):
    if request.method == "POST":
        current_user = request.user
        accomodation = request.POST.get('elt_id')
        accomodation_like = Accomodation.objects.get(
            auto_increment_id=accomodation
            )
        if accomodation_like.likes.filter(id=current_user.id).exists():
            accomodation_like.likes.remove(current_user)
        else:
            accomodation_like.likes.add(current_user)

        return HttpResponseRedirect(accomodation_like.get_absolute_url())


@staff_member_required
def validation_waiting(request):
    validation_waiting = AddAccomodation.objects.filter(
        addAccomodation_statut='Non_lu'
        )

    return render(
        request,
        'accomodation/validation_waiting.html',
        {'validation_waiting': validation_waiting}
        )


@staff_member_required
def validation_checked(request):
    if request.method == 'POST':
        accomodation = request.POST.get('elt_id')
        accomodation_checked = AddAccomodation.objects.get(
            addAccomodation_auto_increment_id=accomodation
            )

        if accomodation_checked.addAccomodation_number is None:
            street = accomodation_checked.addAccomodation_road
        else:
            street = (
                str(accomodation_checked.addAccomodation_number) +
                ' ' +
                accomodation_checked.addAccomodation_road
                )

        url = "https://nominatim.openstreetmap.org/search/<query>?"
        params = {
            "street": street,
            "city": accomodation_checked.addAccomodation_city,
            "postalcode": accomodation_checked.addAccomodation_zipcode,
            "format": 'json',
        }
        req = requests.get(url, params)
        data = req.json()
        accomodation_checked.lat = round(Decimal(data[0]['lat']), 6)
        accomodation_checked.lon = round(Decimal(data[0]['lon']), 6)
        accomodation_checked.save()

        verify = Accomodation.objects.filter(
            lat=accomodation_checked.lat).filter(
            lon=accomodation_checked.lon)
        if not verify:
            new_accommodation = Accomodation(
                name=accomodation_checked.addAccomodation_name,
                category=accomodation_checked.addAccomodation_category,
                number=accomodation_checked.addAccomodation_number,
                road=accomodation_checked.addAccomodation_road,
                zipcode=accomodation_checked.addAccomodation_zipcode,
                city=accomodation_checked.addAccomodation_city,
                phone=accomodation_checked.addAccomodation_phone,
                email=accomodation_checked.addAccomodation_email,
                url=accomodation_checked.addAccomodation_url,
                park=accomodation_checked.addAccomodation_parking,
                image=accomodation_checked.addAccomodation_image,
                description=accomodation_checked.addAccomodation_description,
                lat=accomodation_checked.lat,
                lon=accomodation_checked.lon,
                )
            new_accommodation.save()
            accomodation_checked.delete()
        elif verify:
            accomodation_checked.delete()

    return redirect('accomodation:validation_waiting')


@staff_member_required
def validation_refused(request):
    if request.method == 'POST':
        accomodation = request.POST.get('elt_id')
        accomodation_checked = AddAccomodation.objects.get(
            addAccomodation_auto_increment_id=accomodation
            )
        accomodation_checked.delete()

    return redirect('accomodation:validation_waiting')


def geoloc(request):
    coord = request.GET['coord']
    coord_user = json.loads(coord)
    lat = coord_user[0]
    lon = coord_user[1]

    all_result = Accomodation.objects.all()
    final_result = []
    for elt in all_result:
        dist = 6371 * acos(
            cos(radians(Decimal(lat))) * cos(
                radians(Decimal(elt.lat))) * cos(
                    radians(Decimal(elt.lon)) - radians(
                        Decimal(lon))) + sin(
                            radians(Decimal(lat))) * sin(
                                radians(Decimal(elt.lat))))
        if dist <= 10:
            final_result.append(elt)
    if not final_result:
        return render(request, 'accomodation/noresult.html')

    return render(
        request,
        'accomodation/geoloc.html',
        {'final_result': final_result}
        )
