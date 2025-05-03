from django.contrib import admin
from .models import Product, Collection


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'size', 'color', 'is_featured', 'get_image', 'collection')  # Affiche les bons champs
    search_fields = ('name', 'color', 'collection__name')  # Recherche par nom de produit et collection
    list_filter = ('collection', 'is_featured', 'size')  # Filtres par collection, taille, et mise en avant

    def get_image(self, obj):
        if obj.image_url:
            return f'<img src="{obj.image_url}" width="50" height="50" />'
        elif obj.photo:
            return f'<img src="{obj.photo.url}" width="50" height="50" />'
        return 'No image'

    get_image.allow_tags = True  # Permet d'afficher l'image en HTML dans l'admin


# Enregistrement du modèle Product et Collection dans l'admin
admin.site.register(Product, ProductAdmin)
admin.site.register(Collection)
