from django.shortcuts import render

def complaints(request):
    return render(request, "complaints/complaints.html")