from django.db import models
import random
import string

class ProduktTyp(models.Model):
    TYP_VAL = (
        ('ring', 'Ring'),
        ('halsband', 'Halsband'),
        ('orhange', 'Örhänge'),
        ('armband', 'Armband'),
        ('ovriga', 'Övriga'),
    )
    typ = models.CharField(max_length=20, choices=TYP_VAL)

    def __str__(self):
        return self.typ

class Kategori(models.Model):
    KATEGORI_VAL = (
        ('barnsten', 'Bärnsten'),
        ('smycke', 'Smycke'),
    )
    kategori = models.CharField(max_length=20, choices=KATEGORI_VAL)

    def __str__(self):
        return self.kategori

class Produkt(models.Model):
    METALL_VAL = (
        ('silver', 'Silver'),
        ('guldpleterad', 'Guldpleterad'),
    )
    RING_STORLEKAR = [(x / 10, f"{x / 10:.1f} mm") for x in range(150, 241, 5)]

    KEDJA_LANGDER = tuple((i, f"{i} cm") for i in range(40, 56, 5))

    namn = models.CharField(max_length=200)
    sku = models.CharField(max_length=255, editable=False, blank=True)
    beskrivning = models.TextField()
    vikt = models.FloatField(help_text="Vikt i gram", null=True, blank=True)
    pris = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    inkopspris = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Inköpspris', blank=True)
    antal_i_stycken = models.IntegerField(default=0, blank=True)
    metall = models.CharField(max_length=12, choices=METALL_VAL, default='silver', null=True, blank=True)
    skapad_datum = models.DateTimeField(auto_now_add=True)
    bild = models.ImageField(upload_to='smycken_bilder/', blank=True, null=True)
    produkt_typ = models.ForeignKey(ProduktTyp, on_delete=models.CASCADE)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    ring_storlek = models.FloatField(choices=RING_STORLEKAR, null=True, blank=True)
    kedja_langd = models.PositiveSmallIntegerField(choices=KEDJA_LANGDER, null=True, blank=True)

    def __str__(self):
        return self.namn

    @staticmethod
    def generate_sku():
        # Generera en 8-siffrig SKU bestående av siffror och bokstäver
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

    @staticmethod
    def generate_unique_sku():
        sku = Produkt.generate_sku()
        while Produkt.objects.filter(sku=sku).exists():
            sku = Produkt.generate_sku()
        return sku

    def save(self, *args, **kwargs):
        # Kontrollera om objektet redan har en SKU
        if not self.sku:
            self.sku = self.generate_unique_sku()
        super().save(*args, **kwargs)



