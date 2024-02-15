from django.contrib import admin

# Register your models here.
from .models import MedicineDetails

#admin.site.register(MedicineDetails)
@admin.register(MedicineDetails)
class MedicineDetailsAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'quantity', 'price', 'mfg_date','exp_date')
    fields = ['name', 'quantity', 'price',('mfg_date', 'exp_date')]
