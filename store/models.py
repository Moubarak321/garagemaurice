from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Voiture(models.Model):
    marque = models.CharField(max_length=128)
    slug = models.SlugField(default="slug")
    prix_en_dollars = models.FloatField(default=5000)
    places = models.IntegerField(default=4)
    puissance = models.IntegerField(default=10)
    capacité_du_Reservoir_en_litre = models.IntegerField(default=50)
    caracteristiques_du_moteur_et_details_du_vehicule = models.TextField(max_length=500)
    thumbnail = models.ImageField(upload_to="cars", blank=True, null=True)

    def save(self, *args , **kwargs) :
        self.slug = slugify(self.marque)
        super(Voiture, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("voiture", kwargs = {"slug": self.slug}) # nom de l'url "product" et un paramètre contenant le slug


    def __str__(self):
        return f"{self.marque}"


