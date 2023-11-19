from django.shortcuts import render


def home(request):
    template = 'homepage/main.html'
    context = {}
    return render(request, template, context)
