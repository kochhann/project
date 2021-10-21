# Generated by Django 3.2.8 on 2021-10-21 14:03

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Modificação')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('position', models.CharField(max_length=100, verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Modificação')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('service', models.CharField(max_length=100, verbose_name='Serviço')),
                ('description', models.TextField(max_length=200, verbose_name='Descrição')),
                ('icon', models.CharField(choices=[('lni-cog', 'Engine'), ('lni-stats-up', 'Chart'), ('lni-users', 'User'), ('lni-layers', 'Design'), ('lni-mobile', 'Mobile'), ('lni-rocket', 'Rocket')], max_length=12, verbose_name='Ícone')),
            ],
            options={
                'verbose_name': 'Serviço',
                'verbose_name_plural': 'Serviços',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Modificação')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('bio', models.TextField(max_length=300, verbose_name='Biografia')),
                ('image', stdimage.models.StdImageField(upload_to='team', verbose_name='Imagem,')),
                ('facebook', models.CharField(default='#', max_length=100, verbose_name='Facebook')),
                ('twitter', models.CharField(default='#', max_length=100, verbose_name='Twitter')),
                ('instagram', models.CharField(default='#', max_length=100, verbose_name='Instagram')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.position', verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Funcionário',
                'verbose_name_plural': 'Funcionários',
            },
        ),
    ]