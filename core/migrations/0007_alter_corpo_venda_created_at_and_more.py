# Generated by Django 4.0.2 on 2022-04-28 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_corpo_venda_created_at_formapagamento_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corpo_venda',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='formapagamento',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='saidaprodutos',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
    ]