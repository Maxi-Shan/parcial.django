# Generated by Django 5.0.6 on 2024-09-12 05:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Espacio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('capacidad', models.IntegerField()),
                ('tipo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.cliente')),
                ('espacio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.espacio')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_pago', models.DateTimeField()),
                ('reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.reserva')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_emision', models.DateTimeField(auto_now_add=True)),
                ('total_facturado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Pagada', 'Pagada'), ('Cancelada', 'Cancelada')], max_length=50)),
                ('reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.reserva')),
            ],
        ),
    ]
