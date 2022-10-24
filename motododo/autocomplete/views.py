from django.http import JsonResponse
from accomodation.models import Accomodation


def complete(request):
    searched_term = request.GET.get("term")
    accomodations = Accomodation.objects.filter(city__icontains=searched_term)
    autocomplete_cities = [
        accomodation.city for accomodation in accomodations
        ][:10]
    return JsonResponse(autocomplete_cities, safe=False)
