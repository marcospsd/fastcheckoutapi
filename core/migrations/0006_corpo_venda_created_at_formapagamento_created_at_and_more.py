# Generated by Django 4.0.2 on 2022-04-28 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_saidaprodutos_venda'),
    ]

    operations = [
        migrations.AddField(
            model_name='corpo_venda',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='formapagamento',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='saidaprodutos',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='venda',
            name='create_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
