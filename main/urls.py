from django.urls import path
from .views import MainView, SearchView

app_name = 'main'

urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('search/', SearchView.as_view(), name='search'),
]
