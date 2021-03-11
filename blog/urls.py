from django.urls import path

from blog.views import home
from .views import ListaView, PostagemView, PostagemNovaView, EditarPostagemView, RemoverPostagemView
urlpatterns = [
    path('', home, name="home"),
    path('lista/', ListaView.as_view(), name="lista"),
    path('postagem/<int:pk>/', PostagemView.as_view(), name="postagem"),
    path('postagem/nova/', PostagemNovaView.as_view(), name="nova"),
    path('postagem/<int:pk>/editar', EditarPostagemView.as_view(), name="editar"),
    path('postagem/<int:pk>/remover', RemoverPostagemView.as_view(), name="remover")
]

