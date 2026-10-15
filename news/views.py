from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse("Главная страница новостей")

def index(request):
    return render(request, "news/index.html")

def category(request):
    context = {
        "category_name": "Технологии",
        "articles": [
            "Представлена новая модель смартфона",
            "Компания выпустила обновление программного обеспечения",
            "Учёные разработали новый процессор",
        ],
    }
    return render(request, "news/category.html", context)