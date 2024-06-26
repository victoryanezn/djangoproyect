# Generated by Django 5.0.6 on 2024-06-21 04:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_contacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField()),
                ('descripcion', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='contacto',
            name='correo',
            field=models.EmailField(max_length=254, verbose_name='CORREO:'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='mensaje',
            field=models.TextField(verbose_name='MENSAJE:'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='NOMBRE:'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='color',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.tipo', verbose_name='Tipo'),
        ),
    ]
