from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from django.utils import timezone

from cafe.models import Cafe


class CafeleListView(ListView):
    template_name = 'home.html'
    model = Cafe


def cafeView(request):
    return render(request, 'cafe.html')
