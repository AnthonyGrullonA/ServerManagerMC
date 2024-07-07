from django.db import models
from authentication import models as auth
from django.contrib.auth.models import Group

# Create your models here.


class Industry(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Enterprise(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    website = models.URLField(blank=True)
    logo = models.ImageField(upload_to="enterprise_logos/", null=True, blank=True)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    master_group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name="managed_enterprises"
    )

    def __str__(self):
        return self.name


class UserEnterprise(models.Model):
    user = models.OneToOneField(auth.CustomUser, on_delete=models.CASCADE)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.enterprise.name}"


class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(auth.CustomUser, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username


# Proyectos y Tareas
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    employees = models.ManyToManyField(Employee, related_name="projects")

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
