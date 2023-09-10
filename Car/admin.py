from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class CarAdmin( ImportExportModelAdmin, admin.ModelAdmin):
  list_display = ('Name',  'get_products', 'Car_type')
  search_fields= ('Name',  'get_products', 'Car_type')
  list_filter  = ('Car_type__Name',)
  

class CarTypeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
  
  search_fields = ('Name',)

admin.site.register(models.Car    , CarAdmin)
admin.site.register(models.CarType, CarTypeAdmin)