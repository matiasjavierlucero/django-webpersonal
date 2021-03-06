# Generated by Django 3.2.6 on 2021-09-02 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20210902_2151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titulo')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Creado el')),
                ('updated', models.DateField(auto_now=True, verbose_name='Actualizado el')),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='portfolio',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.categoria'),
        ),
    ]
