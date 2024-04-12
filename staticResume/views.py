from django.shortcuts import render, redirect

# Create your views here.


def static_page(req):
    return redirect("https://kamalpandi.github.io/Portfolio/")
