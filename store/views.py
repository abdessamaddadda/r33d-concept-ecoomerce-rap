from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Collection
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

from .forms import ProfileForm, CardForm  # à créer dans forms.py


# Profil de l'utilisateur
@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm(instance=request.user)
    
    return render(request, 'profile.html', {'form': form})


# Changer le mot de passe
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')  # Redirige vers le profil après changement
    else:
        form = PasswordChangeForm(user=request.user)
    
    return render(request, 'change_password.html', {'form': form})


# Informations de la carte bancaire
@login_required
def card_info(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirige vers le profil après enregistrement des informations de carte
    else:
        form = CardForm()
    
    return render(request, 'card_info.html', {'form': form})


# Page d'inscription
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form': form})


# Page de connexion
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirige vers la page d'accueil après la connexion
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})


# Déconnexion
def logout_view(request):
    logout(request)
    return redirect('login')


def home(request):
    query = request.GET.get('q')
    collection = request.GET.get('collection')
    products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)
    if collection:
        products = products.filter(collection_id=collection)  # filtre par ID

    collections = Collection.objects.all()  # pour dropdown dans le template
    return render(request, 'base.html', {
        'products': products,
        'collections': collections,
    })


def collection_detail(request, collection_id):
    collection = get_object_or_404(Collection, id=collection_id)
    products = Product.objects.filter(collection=collection)
    return render(request, 'collection_detail.html', {
        'collection': collection,
        'products': products
    })


def add_to_cart(request, product_id):
    cart = request.session.get('cart', [])
    if product_id not in cart:
        cart.append(product_id)
        request.session['cart'] = cart
    return redirect('view_cart')


def view_cart(request):
    cart = request.session.get('cart', [])
    products = Product.objects.filter(id__in=cart)
    total = sum([p.price for p in products])
    return render(request, 'cart.html', {'products': products, 'total': total})
