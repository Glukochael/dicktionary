from django.shortcuts import render, redirect
from .models import Word
from .forms import WordForm


def index(request):
    return render(request, 'main/Index.html')


def word_list(request):
    words = Word.objects.all()
    return render(request, 'main/word_list.html', {'words': words})


def search(request):
    return render(request, 'main/Search.html')


def adding(request):
    error = ''
    if request.method == "POST":
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('word-list')
        else:
            error = "Неверно заполненны данные"
    form = WordForm()
    context = {
        'form': form
    }
    return render(request, 'main/adding.html', context, error)
