# Generated by Django 4.0.1 on 2022-01-18 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ventas', '0003_alter_venta_producto_delete_orden'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='ordenado',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='producto',
        ),
        migrations.AddField(
            model_name='venta',
            name='venta',
            field=models.FileField(blank=True, null=True, upload_to='facturas'),
        ),
    ]