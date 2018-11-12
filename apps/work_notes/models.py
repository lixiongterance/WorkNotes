from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    """note"""
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    parent_dir = models.ForeignKey('Dir', on_delete=models.CASCADE, null=True,
                                   blank=True, default=None)
    user = models.ForeignKey(User)

    class Meta:
        verbose_name_plural = 'Notes'

    def __str__(self):
        return self.title

class Dir(models.Model):
    """dir"""
    name = models.CharField(max_length=200)
    desc = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    parent_dir = models.ForeignKey('self', on_delete=models.CASCADE, null=True,
                                   blank=True, default=None)
    user = models.ForeignKey(User)

    class Meta:
        unique_together=('parent_dir', 'name')
    
    def __str__(self):
        return self.name
