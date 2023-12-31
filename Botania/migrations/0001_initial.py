# Generated by Django 4.2.3 on 2023-07-07 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='catalogo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('tamaño', models.CharField(max_length=30)),
                ('temporada', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=30)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('moneda', models.CharField(default='CLP', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='tipo_usuario',
            fields=[
                ('idtipo_usuario', models.AutoField(db_column='idtipo', primary_key=True, serialize=False, verbose_name='id_tipo_usuario')),
                ('tipo_usuario', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apaterno', models.CharField(max_length=30)),
                ('amaterno', models.CharField(max_length=30)),
                ('correo', models.EmailField(max_length=100, unique=True)),
                ('clave', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=10)),
                ('region', models.CharField(max_length=50)),
                ('provincia', models.CharField(max_length=50)),
                ('comuna', models.CharField(max_length=50)),
                ('codpos', models.CharField(max_length=7)),
                ('tipo_usuario', models.ForeignKey(db_column='idtipo', on_delete=django.db.models.deletion.CASCADE, to='Botania.tipo_usuario')),
            ],
        ),
    ]
