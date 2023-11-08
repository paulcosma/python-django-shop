from django.urls import path
from . import views

# /products
# /products/1/detail
# /products/new
urlpatterns = [
    # not calling views.index. I am simply passing a reference to it.
    # django will take care of calling views.index() function at runtime
    # when the client sends an http request to the server
    path('', views.index),
    path('new', views.new_products)
]

