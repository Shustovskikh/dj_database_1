from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    image = models.ImageField(upload_to='phones/')
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)