# Generated by Django 4.0.1 on 2022-01-05 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0002_rename_uniades_producto_unidad'),
        ('Ventas', '0002_venta_ordenado_alter_venta_vendedor_orden_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='producto',
            field=models.ManyToManyField(to='Gestion.Producto'),
        ),
        migrations.DeleteModel(
            name='Orden',
        ),
    ]
