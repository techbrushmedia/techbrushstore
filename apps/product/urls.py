from django.urls import path
from .views import CategoryDetailView, ProductListView, ProductDetailView
urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
]