from django.contrib.auth.models import User
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from ast import literal_eval
from django.contrib import messages

from .models import Product, Favorite


def search_sub(request):
    """Searches for substitutes at user's request"""

    try:
        filter_type = 'product_name__icontains'
        keyword = request.GET.get('q')
        queryset_list = Product.objects.filter(**{filter_type: keyword})
        context = {'found_substitute': queryset_list}
    except Product.DoesNotExist:
        raise Http404("Ce produit n'existe pas.")
    return render(request, 'products/products.html', context)


def sub_details(request, product_id):
    """Displays details of a selected substitute"""

    try:
        sub = Product.objects.get(id=product_id)
        nutri_dict = literal_eval(sub.nutri_values)
        Product.transl_nutri_keys(nutri_dict)
        nutriments = {}
        for i in sorted(nutri_dict):
            nutriments[i] = nutri_dict[i]
        context = {'substitute': sub, 'nutriments': nutriments}
    except Product.DoesNotExist:
        raise Http404("Ce produit n'existe pas.")
    return render(request, 'products/product_details.html',
                  context)


def save_sub(request, product_id):
    """Saves a product to the user's favorites"""

    try:
        sub = Product.objects.get(id=product_id)
        Favorite.objects.create(user=request.user, product=sub)
        messages.success(request, 'Votre produit a bien été sauvegardé dans vos favoris!')
    except Exception as e:
        messages.error(request, 'Ce produit est déjà enregistré dans vos favoris!')
    return redirect('favorites')


def favorite_sub(request):
    """Render user's saved products"""

    try:
        fav_subs = Favorite.objects.filter(user=request.user)
        context = {'fav_subs': fav_subs}
    except Exception as e:
        messages.error(request, "Vous n'avez pas de produits enregistrés pour le moment!")
    return render(request, 'products/favorites.html', context)

def delete_fav(request, product_id):
    """Render user's saved products"""

    try:
        Favorite.objects.filter(user=request.user, product=product_id).delete()
    except Exception as e:
        messages.error(request, "Vous n'avez pas de produits enregistrés pour le moment!")
    return redirect('favorites')
