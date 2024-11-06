from django.contrib import admin
from aplication.models import Folga

# Register your models here.

@admin.register(Folga)
class folga(admin.ModelAdmin):
    list_display = ['day','motivo','folga_pessoa', 'status_folga']