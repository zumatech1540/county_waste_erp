from django.shortcuts import render

def gis_dashboard(request):
    return render(request, "gis/dashboard.html")