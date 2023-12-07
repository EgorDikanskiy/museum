from django.shortcuts import render


def persons(request):
    template = 'persons/persons.html'
    context = {}
    return render(request, template, context)


def persons_detailed(request):
    template = 'persons/persons_detailed.html'
    context = {}
    return render(request, template, context)
