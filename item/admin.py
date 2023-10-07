from django.contrib import admin
from .models import Category, Item,Ticket
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class ItemImportExport(ImportExportModelAdmin, admin.ModelAdmin):
  search_fields = ('name',  'category__name');
  list_display  = ('name', 'category', 'price', 'Supported_cars');
  list_filter   = ( 'category__name','is_sold');
  

admin.site.register(Category); 
admin.site.register(Item, ItemImportExport); 
admin.site.register(Ticket)