from django.contrib import admin
from aplication.models import Folga, Ferias

# Register your models here.

@admin.register(Folga)
class folga(admin.ModelAdmin):
    list_display = ['day','motivo','folga_pessoa','unit', 'status_folga']

@admin.register(Ferias)
class Feria(admin.ModelAdmin):
    list_display = ['pessoa_vacation', 'start_vacation','end_vacation' ]