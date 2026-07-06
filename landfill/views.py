from django.shortcuts import render

def truck_entries(request):
    return render(request, "landfill/truck_entries.html")