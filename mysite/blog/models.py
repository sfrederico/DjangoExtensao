from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    """
        Model que define as postagens do blog como objetos.
    """
    ##Atributos
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    text = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)
    data_pub = models.DateTimeField(blank=True, null=True)

    ##Métodos
    def __str__(self) -> str:
        return f'{self.titulo} de {self.autor}'
    
class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data = models.DateField(default=timezone.now)
    texto = models.TextField()

    def __str__(self) -> str:
        return f'{self.autor} em {self.post}'