from django.urls import path

from . import views

urlpatterns = [
    path('', views.search_sub, name='search_results'),
    path('favorites/', views.favorite_sub, name='favorites'),
    path('<int:product_id>/', views.sub_details, name='product_details'),
    path('save/<int:product_id>/', views.save_sub, name='save'),
    path('unsave/<int:product_id>/', views.delete_fav, name='del_fav'),
]