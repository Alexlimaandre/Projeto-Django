from django.db import models
from datetime import datetime


#  class nome_classe(refencia a classe pai):
class Todo(models.Model):
    title = models.CharField(verbose_name="Título", max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(verbose_name="Prazo", null=False, blank=False)
    finished_at = models.DateField(verbose_name="Concluído em", null=True)
    
    class Meta:
        ordering = ["finished_at", "deadline"]
        
    
    def mark_as_finished(self):
        if not self.finished_at:
            self.finished_at = datetime.now()
            self.save()
