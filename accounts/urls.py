from django.urls import path 
from django.views.generic.base import RedirectView

from .views import * 

urlpatterns = [
    
    path('',index,name='index'),
    path('next-page',nextp,name='next-page'),
    path('go-to-mawdo3at/',RedirectView.as_view(url='https://www.mawdo3at.com/2020/09/Curious-information-about-psychology.html'), name='go-to-mawdo3at'),
]

