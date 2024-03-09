from django.shortcuts import render

# Create your views here.


def static_page(req):
    return render(req, 'index.html')
