# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Inventory, CellConfiguration, InventoryElement, Cell
from .forms import InventoryForm, CellConfigurationForm

class InventoryCreateView(View):
    def get(self, request):
        inventory_form = InventoryForm()
        return render(request, 'inventory/inventory_create.html', {
            'inventory_form': inventory_form,
        })

    def post(self, request):
        inventory_form = InventoryForm(request.POST)
        if inventory_form.is_valid():
            inventory = inventory_form.save()
            return redirect('inventory_detail', pk=inventory.pk)

        return render(request, 'inventory/inventory_create.html', {
            'inventory_form': inventory_form,
        })

class CellConfigurationCreateView(View):
    def get(self, request, inventory_id):
        inventory = get_object_or_404(Inventory, pk=inventory_id)
        cell_config_form = CellConfigurationForm()
        return render(request, 'inventory/cell_configuration_create.html', {
            'inventory': inventory,
            'cell_config_form': cell_config_form,
        })

    def post(self, request, inventory_id):
        inventory = get_object_or_404(Inventory, pk=inventory_id)
        cell_config_form = CellConfigurationForm(request.POST)
        if cell_config_form.is_valid():
            configuration = cell_config_form.save(commit=False)
            configuration.inventory = inventory
            configuration.save()
            return redirect('inventory_detail', pk=inventory.pk)

        return render(request, 'inventory/cell_configuration_create.html', {
            'inventory': inventory,
            'cell_config_form': cell_config_form,
        })

class InventoryDetailView(View):
    def get(self, request, pk):
        inventory = get_object_or_404(Inventory, pk=pk)
        cell_configurations = inventory.cell_configurations.all()
        elements = inventory.elements.all()
        return render(request, 'inventory/inventory_detail.html', {
            'inventory': inventory,
            'cell_configurations': cell_configurations,
            'elements': elements,
        })

class InventoryElementCreateView(View):
    def get(self, request, inventory_id):
        inventory = get_object_or_404(Inventory, pk=inventory_id)
        return render(request, 'inventory/element_create.html', {
            'inventory': inventory,
        })

    def post(self, request, inventory_id):
        inventory = get_object_or_404(Inventory, pk=inventory_id)
        label = request.POST.get('label')
        if label:
            element = InventoryElement.objects.create(inventory=inventory, label=label)
            # Create cells for each configuration associated with the inventory
            for config in inventory.cell_configurations.all():
                Cell.objects.create(element=element, configuration=config)
            return redirect('inventory_detail', pk=inventory.pk)

        return render(request, 'inventory/element_create.html', {
            'inventory': inventory,
        })
