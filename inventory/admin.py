from django.contrib import admin
from .models import Inventory, CellConfiguration, InventoryElement, Cell

# Register your models here.

class CellInline(admin.TabularInline):
    model = Cell
    extra = 0

class InventoryElementInline(admin.TabularInline):
    model = InventoryElement
    extra = 0

class InventoryAdmin(admin.ModelAdmin):
    inlines = [
        InventoryElementInline,
    ]

class CellConfigurationAdmin(admin.ModelAdmin):
    inlines = [
        CellInline,
    ]

admin.site.register(Inventory, InventoryAdmin)
admin.site.register(CellConfiguration, CellConfigurationAdmin)
admin.site.register(InventoryElement)
admin.site.register(Cell)
