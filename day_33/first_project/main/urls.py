from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('render_html/', views.render_html, name='render_html')
]
