from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'home.html', context)


def header(request, *args, **kwargs):
    context = {}
    return render(request, 'shared/header.html', context)


def footer(request, *args, **kwargs):
    context = {}
    return render(request, 'shared/footer.html', context)


def contact_us(request):
    context = {}
    return render(request, 'contact-us.html', context)
