from django.db import models
import datetime

class Gif(models.Model):
    image = models.ImageField(upload_to='gifs')
    rating = models.DecimalField(default=1500, max_digits=7, decimal_places=2)
    rating_deviation = models.DecimalField(default=350, max_digits=7, decimal_places=2)
    last_updated = models.DateTimeField(auto_now=True, default=datetime.datetime(2000,1,1))
