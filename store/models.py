from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"
class CardInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)
    expiry_date = models.CharField(max_length=5)  # MM/YY
    cvv = models.CharField(max_length=3)
class Collection(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)  # Ajout d'une description pour plus de détails

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(null=True, blank=True)  # URL de l'image
    photo = models.ImageField(upload_to='products/', null=True, blank=True)  # Image à télécharger manuellement
    size = models.CharField(max_length=10, default="M")
    color = models.CharField(max_length=50, default="Noir")
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, null=True)
    is_featured = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.size}, {self.color})"

    def clean(self):
        if self.price < 0:
            raise ValidationError("Le prix ne peut pas être négatif.")
