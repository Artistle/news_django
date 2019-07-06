from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class News(models.Model):

    title = models.CharField(max_length=200)
    text = models.TextField("auhor", null=True)
    tag = models.CharField("Tag", null=True,max_length=20)
    image = models.ImageField("Изображение", upload_to="catalog/media/",null=True, blank=True)

    def __str__(self):

        return self.title

    def get_absolute_url(self):

        return reverse('news-detail', args=[str(self.id)])
