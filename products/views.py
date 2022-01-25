from django.http import Http404
from django.shortcuts import render, redirect
from ast import literal_eval

from .models import Product, Favorite


def search_sub(request):
    """Searches for substitutes at user's request"""

    try:
        filter_type = 'product_name__icontains'
        keyword = request.GET.get('q')
        qs_list = Product.objects.filter(**{filter_type: keyword})
        sub_qs = qs_list.all()[:1]
        sub_qs_value = list(sub_qs.values_list('nutriscore', flat=True))
        if sub_qs_value == ["A"]:
            qs_list = qs_list.filter().exclude(nutriscore__range=("B", "E"))
        if sub_qs_value == ["B"]:
            qs_list = qs_list.filter().exclude(nutriscore__range=("C", "E"))
        elif sub_qs_value == ["C"]:
            qs_list = qs_list.filter().exclude(nutriscore__range=("D", "E"))
        elif sub_qs_value == ["D"] or sub_qs_value == ["E"]:
            qs_list = qs_list.filter().exclude(nutriscore__exact="E")
        context = {'found_substitute': qs_list}
    except Exception:
        raise Http404
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
    except Exception:
        raise Http404
    return render(request, 'products/product_details.html',
                  context)


def save_sub(request, product_id):
    """Saves a product to the user's favorites"""

    try:
        user = request.user
        if user.is_authenticated:
            sub = Product.objects.get(id=product_id)
            Favorite.objects.create(user=request.user, product=sub)
        else:
            raise Exception
    except Exception:
        raise Http404
    return redirect('favorites')


def favorite_sub(request):
    """Render user's saved products"""

    try:
        user = request.user
        if user.is_authenticated:
            fav_subs = Favorite.objects.filter(user=request.user)
            context = {'fav_subs': fav_subs}
        else:
            raise Exception
    except Exception:
        raise Http404
    return render(request, 'products/favorites.html', context)


def delete_fav(request, product_id):
    """Render user's saved products after deleting"""

    try:
        user = request.user
        if user.is_authenticated:
            Favorite.objects.filter(user=request.user,
                                    product=product_id).delete()
        else:
            raise Exception
    except Exception:
        raise Http404
    return redirect('favorites')
