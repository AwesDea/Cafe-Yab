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

            return render(request, 'home.html', {'form': form, 'results': results})
    else:
        form = searchInCafes()
    return render(request, 'home.html', {'form': form})


def cafeView(request, cafe_id):
    cafe = get_object_or_404(Cafe, pk=cafe_id)
    return render(request, 'cafe.html', {'cafe': cafe,
                                                  })
