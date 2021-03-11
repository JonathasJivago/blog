from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Postagem
from django.urls import reverse_lazy
# Create your views here.
def home(request):
    return render(request, "blog/blog_base.html", {})


class ListaView(ListView):
    model = Postagem
    template_name = "blog/lista.html"
    context_object_name = "minhas_postagens"

class PostagemView(DetailView):
    model = Postagem
    template_name = "blog/postagem.html"

class PostagemNovaView(CreateView):
    model = Postagem
    template_name = "blog/nova_postagem.html"
    fields = ['titulo', 'conteudo', 'autor', 'status']

class EditarPostagemView(UpdateView):
    model = Postagem
    template_name = "blog/editar_postagem.html"
    fields = ['titulo', 'conteudo', 'status']

class RemoverPostagemView(DeleteView):
    model = Postagem
    template_name = "blog/remover_postagem.html"
    success_url = reverse_lazy('lista')