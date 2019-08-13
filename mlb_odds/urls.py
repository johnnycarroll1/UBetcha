from django.urls import path
from . import views

app_name = 'mlb_odds'

urlpatterns = [
    path('mlb_odds/', views.index, name="MLB Odds"),
]
