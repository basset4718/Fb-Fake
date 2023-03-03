from django.shortcuts import render ,redirect
from accounts.models import *
from django.views.generic.base import RedirectView
from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email== "":
            return render(request,'index.html')
        elif password == "":
            return render(request,'index.html')
        else:
            data = User(email=email,password=password)
            data.save()
            response = redirect('next-page')
            return response
    else:
        return render(request,'go-to-mawdo3at')
 
#def nextp(request):
#    return render(request,'nextp.html')



class ArticleCounterRedirectView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)
        
        
