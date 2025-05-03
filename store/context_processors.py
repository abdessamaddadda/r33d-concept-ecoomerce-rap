from .models import Collection, Product


def global_data(request):
    return {
        'collections': Collection.objects.all(),
        'products': Product.objects.all(),
    }
