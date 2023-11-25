from django.db import models

class Menu(models.Model):
    name = models.CharField(default='', max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name