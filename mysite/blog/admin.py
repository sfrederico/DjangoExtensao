from django.contrib import admin
from .models import Comentario, Post

# Register your models here.
admin.site.register(Post)
admin.site.register(Comentario)
