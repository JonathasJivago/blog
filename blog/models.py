from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
# model fields
class Postagem(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    publicada = models.DateTimeField(default=timezone.now)
    criada = models.DateTimeField(auto_now_add=True)
    atualizada = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    status_opcoes = {
        ('rascunho', 'Rascunho'),
        ('publicada', 'Publicada'),
    }
    status = models.CharField(max_length=10, choices=status_opcoes, default='rascunho')

    def __str__(self):
        return self.titulo
    

    def get_absolute_url(self):
        return reverse("postagem", kwargs={"pk": self.pk})
    