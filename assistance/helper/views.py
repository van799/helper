from django.shortcuts import render, redirect, get_object_or_404

from .models import Table
from .forms import TableForm


def index(request):
    template = 'helper/index.html'
    text = Table.objects.all()
    # month = Table.objects.filter(time=)
    context = {
        'text': text,
    }
    return render(request, template, context)


def create_helper(request):
    template = 'helper/create_helper.html'
    form = TableForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('helper:index')
    return render(request, template, {"form": form})

