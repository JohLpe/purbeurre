from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def mentions(request):
    return render(request, 'mentions.html')


def error_404(request, exception):
    return render(request, '404.html')


def error_500(request):
    return render(request, '500.html')
