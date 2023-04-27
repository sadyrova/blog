from django.shortcuts import redirect, render
from tovars.models import Tovar

from tovars.forms import TovarCreateForm, ReviewCreateForm

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

def tovar_detail_view(request, id):
    if request.method =='GET':
        tovar = Tovar.objects.get(id=id)

        context = {
            'tovar': tovar,
            'comments': tovar.comment_set.all()
        }
        return render(request, 'tovars/detail.html', context=context)

def tovar_create_view(request):
    if request.method == 'GET':
        context = {
            'form': TovarCreateForm
        }
        return render(request,'tovars/create.html', context=context)

    if request.method =='POST':
        data, files = request.POST, request.FILES
        form = TovarCreateForm(data, files)

        if form.is_valid():
            Tovar.objects.create(
                image=form.cleaned_data.get('image'),
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data.get('price'),
                quantity=form.cleaned_data.get('quantity')
            )


            return redirect('/tovars/')

        return render(request, 'tovars/create.html', context={
            'form': form
        })

def review_create_view(request):
    if request.method == 'GET':
        context = {
            'form': ReviewCreateForm
        }
        return render(request,'tovars/create.html', context=context)

    if request.method =='POST':
        data = request.POST
        form = ReviewCreateForm(data)

        if form.is_valid():
            Tovar.objects.create(
                comment=form.cleaned_data.get('comment')

            )

            return redirect('/tovars/')

        return render(request, 'tovars/create.html', context={
            'form': form
        })



