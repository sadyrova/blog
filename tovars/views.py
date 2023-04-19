from django.shortcuts import render
from tovars.models import Tovar

# Create your views here.

def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')

def tovar_view(request):
    if request.method == 'GET':
        tovars = Tovar.objects.all()

        context = {
            'tovars':tovars
        }

        return render(request, 'tovars/tovars.html', context=context)
