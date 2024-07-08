# urls.py

from django.urls import path
from .views import InventoryCreateView, CellConfigurationCreateView, InventoryDetailView, InventoryElementCreateView

urlpatterns = [
    path('inventory/new/', InventoryCreateView.as_view(), name='inventory_create'),
    path('inventory/<int:pk>/', InventoryDetailView.as_view(), name='inventory_detail'),
    path('inventory/<int:inventory_id>/cell/new/', CellConfigurationCreateView.as_view(), name='cell_config_create'),
    path('inventory/<int:inventory_id>/element/new/', InventoryElementCreateView.as_view(), name='element_create'),
]
