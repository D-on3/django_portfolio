from django.db import models

class SliderImage(models.Model):
    image = models.ImageField(upload_to='slider_images/')
    caption = models.CharField(max_length=255)
    app_link = models.CharField(max_length=255)

    def __str__(self):
        return self.caption