from django.urls import path
from portfolioapp import views

urlpatterns = [
    path('', views.index,name='index'),
    path('Display/', views.display,name='Display'),
    path('About', views.about, name='About'),
    path('Profile', views.profile, name='Profile'),
]
