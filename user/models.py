from django.db import models

class Contacts(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['first_name']
        verbose_name_plural = "Kontaklar"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

