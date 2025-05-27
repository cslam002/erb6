from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse ("<h1>Hello World</h1>")
    # pages_url = reverse('pages:index')
    return render(request, 'pages/index.html')

def about(request):
    # pages_url = reverse('pages:about')
    return render(request, 'pages/about.html')
