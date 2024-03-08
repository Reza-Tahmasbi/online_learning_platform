from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Rating(models.Model):
    RATING_CHOICES = (
        (0.5, '0.5'),
        (1.0, '1.0'),
        (1.5, '1.5'),
        (2.0, '2.0'),
        (2.5, '2.5'),
        (3.0, '3.0'),
        (3.5, '3.5'),
        (4.0, '4.0'),
        (4.5, '4.5'),
        (5.0, '5.0'),
    )
    rating = models.FloatField(choices=RATING_CHOICES, default = 4)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    
    def __str__(self):
        return f"{self.content_object} - Rating: {self.rating}"