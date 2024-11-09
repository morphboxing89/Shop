from django.http import HttpResponse
from django.shortcuts import render

# from goods.models import Categories


def index(request) -> HttpResponse:

    context: dict = {
        'title': 'moRph - Главная',
        'content': 'Магазин мебели moRph',
    }
    return render(request, 'main/index.html', context)


def about(request) -> HttpResponse:
    context: dict = {
        'title': 'moRph - О нас',
        'content': 'О нас',
        'text_on_page': 'В мой магазин люит ходить Олег Олегович Цкахая. В наличие имеется кальян на свинине'
    }
    return render(request, 'main/about.html', context)
