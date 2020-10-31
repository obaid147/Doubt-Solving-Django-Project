from django.db import models


class Pdf(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs')

    def __str__(self):
        return self.title
    
    