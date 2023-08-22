from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Produkt, ProduktTyp, Kategori
from import_export.admin import ImportExportModelAdmin
from .resources import ProduktResource, ProduktTypResource, KategoriResource
from django.utils.html import mark_safe



@admin.register(Produkt)
class ProduktAdmin(ImportExportModelAdmin):
    resource_class = ProduktResource
    list_display = ['namn', 'sku', 'pris', 'inkopspris', 'display_thumbnail']
    readonly_fields = ['sku', 'skapad_datum']
    search_fields = ['namn', 'sku', 'pris']
    list_filter = ('antal_i_stycken', 'metall', 'kategori')

    def display_thumbnail(self, obj):
        if obj.bild:
            return mark_safe(f'<img src="{obj.bild.url}" width="60" height="70" />')
        return None


@admin.register(ProduktTyp)
class ProduktTypAdmin(ImportExportModelAdmin):
    resource_class = ProduktTypResource
    list_display = ('typ',)

@admin.register(Kategori)
class KategoriAdmin(ImportExportModelAdmin):
    resource_class = KategoriResource
    list_display = ('kategori',)