from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
# Create your views here.
# class home(TemplateView):
#     template_name = 'home.html'


def home(request):
    contexto = {
        'nome': 'João',
        'idade': 30
    }
    return render(request, "home.html", contexto)



# def home(request):
#     template = loader.get_template("home.html")
#     context = {
#         'nome': 'João',
#         'idade': 20
#     }
#     return HttpResponse(template.render(context, request))




# def home(request):
#     return HttpResponse('<h1>Boas Vindas!</h1>')

def sobre(request):
    return HttpResponse("Você está na página sobre o site!")