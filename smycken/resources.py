# smycken/resources.py

from import_export import resources
from .models import Produkt, ProduktTyp, Kategori

class ProduktResource(resources.ModelResource):
    class Meta:
        model = Produkt

class ProduktTypResource(resources.ModelResource):
    class Meta:
        model = ProduktTyp

class KategoriResource(resources.ModelResource):
    class Meta:
        model = Kategori
