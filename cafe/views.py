import json
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views.generic.list import ListView
from django.utils import timezone

from account.forms.forms import SearchForm
from cafe.models import Cafe


class CafeleListView(ListView):
    template_name = 'home.html'
    model = Cafe


def searchInCafes(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            keyword = form.cleaned_data.get('keyword')
            results = Cafe.objects.filter(name__contains=keyword)

            return render(request, 'home.html', {'form': form, 'object_list': results})
    else:
        form = searchInCafes()
    return render(request, 'home.html', {'form': form})


def cafeView(request, cafe_id):
    cafe = get_object_or_404(Cafe, pk=cafe_id)
    return render(request, 'cafe.html', {'cafe': cafe,
                                                  })


def autocomplete(request):
    print('salam')
    if request.is_ajax():
        q = request.GET.get('term', '')
        cafes = Cafe.objects.filter(name__icontains=q)[:20]
        results = []
        for cafe in cafes:
            cafe_json = {}
            cafe_json['id'] = cafe.id
            cafe_json['name'] = cafe.name
            results.append(cafe_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

