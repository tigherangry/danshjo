from django.db import models

class danshjo(models.Model):
    name = models.CharField(max_length=50)
    family = models.CharField(max_length=500)
    dad= models.CharField(max_length=500)
    number= models.CharField(max_length=500)
    phone= models.CharField(max_length=500)
    subject= models.CharField(max_length=500)
    def __str__(self):
        return self.name

# comment
class notebock(models.Model):
    nameNote = models.CharField(max_length=50)
    text = models.CharField()

    def __str__(self):
        return self.nameNote