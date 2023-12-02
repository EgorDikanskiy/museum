from django.shortcuts import render


def history(request):
    template = 'history/history.html'
    context = {}
    return render(request, template, context)


def history_detailed(request):
    template = 'history/history_detailed.html'
    context = {}
    return render(request, template, context)
