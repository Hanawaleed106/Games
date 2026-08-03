from django.shortcuts import render

def game1(request):
    return render(request, "pages/game1.html")

def game2(request):
    return render(request, "pages/game2.html")

def game3(request):
    return render(request,"pages/game3.html")

