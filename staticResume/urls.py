from django.urls import include, path
from .views import static_page

urlpatterns = [
    path('', static_page),
]

