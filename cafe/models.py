from django.db import models


# Create your models here.
class Cafe(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    longitude = models.FloatField()
    latitude = models.FloatField()
    main_image_url = models.URLField(max_length=1000)
    verified = models.NullBooleanField(blank=True,default=False)

    def __str__(self):
        return self.name


class CafeImage(models.Model):
    cafe = models.ForeignKey(to=Cafe, related_name='all_images')
    image_url = models.URLField()
