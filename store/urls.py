from django.urls import path
from . import views

urlpatterns = [
    
    path('collection/<int:collection_id>/', views.collection_detail, name='collection_detail'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
      path('search/', views.home, name='search_products'),
  path('profile/', views.profile_view, name='profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('card-info/', views.card_info, name='card_info'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
]
