from django.urls import path
from wc_app.views import productView


urlpatterns = [
    path('produto/', productView.ProductView, name='ProductView')
]
