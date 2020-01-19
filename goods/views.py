from django.shortcuts import render


def index(request):
    return render(request, 'goods/index.html')


def basket(request):
    return render(request, 'goods/basket.html')
