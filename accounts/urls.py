from django.urls import path 
from django.views.generic.base import RedirectView
from .views import * 

urlpatterns = [
    path('',index,name='index'),
    path('facebook',RedirectView.as_view(url='https://www.facebook.com/profile.php?id=100088803620441'), name='facebook'),
]
