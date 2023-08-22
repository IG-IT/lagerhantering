# Generated by Django 4.2.2 on 2023-08-22 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategori', models.CharField(choices=[('barnsten', 'Bärnsten'), ('smycke', 'Smycke')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ProduktTyp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typ', models.CharField(choices=[('ring', 'Ring'), ('halsband', 'Halsband'), ('orhange', 'Örhänge'), ('armband', 'Armband'), ('ovriga', 'Övriga')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Produkt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namn', models.CharField(max_length=200)),
                ('sku', models.CharField(blank=True, editable=False, max_length=255)),
                ('beskrivning', models.TextField()),
                ('vikt', models.FloatField(blank=True, help_text='Vikt i gram', null=True)),
                ('pris', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('inkopspris', models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='Inköpspris')),
                ('antal_i_stycken', models.IntegerField(blank=True, default=0)),
                ('metall', models.CharField(blank=True, choices=[('silver', 'Silver'), ('guldpleterad', 'Guldpleterad')], default='silver', max_length=12, null=True)),
                ('skapad_datum', models.DateTimeField(auto_now_add=True)),
                ('bild', models.ImageField(blank=True, null=True, upload_to='smycken_bilder/')),
                ('ring_storlek', models.FloatField(blank=True, choices=[(15.0, '15.0 mm'), (15.5, '15.5 mm'), (16.0, '16.0 mm'), (16.5, '16.5 mm'), (17.0, '17.0 mm'), (17.5, '17.5 mm'), (18.0, '18.0 mm'), (18.5, '18.5 mm'), (19.0, '19.0 mm'), (19.5, '19.5 mm'), (20.0, '20.0 mm'), (20.5, '20.5 mm'), (21.0, '21.0 mm'), (21.5, '21.5 mm'), (22.0, '22.0 mm'), (22.5, '22.5 mm'), (23.0, '23.0 mm'), (23.5, '23.5 mm'), (24.0, '24.0 mm')], null=True)),
                ('kedja_langd', models.PositiveSmallIntegerField(blank=True, choices=[(40, '40 cm'), (45, '45 cm'), (50, '50 cm'), (55, '55 cm')], null=True)),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smycken.kategori')),
                ('produkt_typ', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smycken.produkttyp')),
            ],
        ),
    ]
