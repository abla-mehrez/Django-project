# Generated by Django 4.0.5 on 2022-06-23 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GestionElectro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('date', models.DateTimeField(null=True)),
                ('quantité', models.IntegerField(default=0)),
                ('prixTotal', models.FloatField(default=0)),
                ('client', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='GestionElectro.client')),
                ('product', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='GestionElectro.produit')),
            ],
        ),
    ]
