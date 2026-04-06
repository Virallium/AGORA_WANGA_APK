from django.urls import path
from . import views
urlpatterns = [
    path('',views.Accueil, name="Accueil"),
    path('Evenements/', views.evenements, name="evenement"),
    path('Services/',views.services, name="services"),
    path('Blog/', views.blog, name="blog"),
    path('Apropos/', views.Apropos, name="Apropos"),
    path('Carte/', views.carte, name="carte")
]
