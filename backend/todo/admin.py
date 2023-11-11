from django.contrib import admin
from .models import Todo

# Register your models here.
# create a class for the admin-model integration
class TodoAdmin(admin.ModelAdmin):
    # add the fields of the model here
    list_display = ("titulo","descricao","completa")
  
# we will need to register the
# model class and the Admin model class
# using the register() method
# of admin.site class
admin.site.register(Todo,TodoAdmin)