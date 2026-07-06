from django.shortcuts import render

def routes(request):
    return render(request, "collection/routes.html")