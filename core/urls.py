from django.contrib import admin
from django.urls import path
from api.views import add_phone,model_phones,search_name,upd_phone,sign_in,sign_up,add_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_phone/',add_phone),
    path('get_model/',model_phones),
    path('get_phone/',search_name),
    path('upd_phone/',upd_phone),
    path('sign_in/',sign_in),
    path('sign_up/',sign_up),
    path('add_product/<int:pk>',add_product),
]
