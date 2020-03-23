from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    class Meta:
        db_table='Category'
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name

class Todo(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    category= models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    #complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table='Todo'
        verbose_name_plural='Todos'

