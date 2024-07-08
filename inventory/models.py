# models.py

from django.db import models

class Inventory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class CellConfiguration(models.Model):
    TYPE_CHOICES = [
        ('TEXT', 'Text'),
        ('NUMBER', 'Number'),
        ('TASK_COMPLETED', 'Task Completed'),
        ('DISPLAY_BOX', 'Display Box'),
    ]

    inventory = models.ForeignKey(Inventory, related_name='cell_configurations', on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    cell_type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.label} - {self.get_cell_type_display()}"

class InventoryElement(models.Model):
    inventory = models.ForeignKey(Inventory, related_name='elements', on_delete=models.CASCADE)
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label

class Cell(models.Model):
    element = models.ForeignKey(InventoryElement, related_name='cells', on_delete=models.CASCADE)
    configuration = models.ForeignKey(CellConfiguration, on_delete=models.CASCADE)
    value_text = models.TextField(blank=True, null=True)
    value_number = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    value_boolean = models.BooleanField(default=False)
    value_datetime = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.configuration.label} - {self.element.label}"
