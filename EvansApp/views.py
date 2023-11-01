from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "index.html")
def gal(request):
    return render(request, "gallery-single.html")
def about(request):
    return render(request, "about.html")
def gallery(request):
    return render(request, "gallery.html")
def contact(request):
    return render(request, "contact.html")

def services(request):
    return render(request, "services.html")
def sample(request):
    return render(request, "sample-inner-page.html")
