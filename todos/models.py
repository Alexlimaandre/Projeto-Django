from django.db import models


#  class nome_classe(refencia a classe pai):
class Todo(models.Model):
    title = models.CharField(verbose_name="Título", max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(verbose_name="Prazo", null=False, blank=False)
    finished_at = models.DateField(verbose_name="Concluído em", null=True)
