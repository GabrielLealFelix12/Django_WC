from django.urls import path
from wc_app.views import productView
from wc_app.views import homeView


urlpatterns = [
    path('produto/', productView.ProductView, name='ProductView'),
    path('', homeView.HomeView, name='HomeView')
]
