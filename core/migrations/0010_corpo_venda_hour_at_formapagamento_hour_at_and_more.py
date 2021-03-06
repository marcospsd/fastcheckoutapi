# Generated by Django 4.0.2 on 2022-04-29 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_corpo_venda_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='corpo_venda',
            name='hour_at',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='formapagamento',
            name='hour_at',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='venda',
            name='hour_at',
            field=models.TimeField(auto_now=True),
        ),
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
            model_name='venda',
            name='create_at',
            field=models.DateField(auto_now=True),
        ),
    ]
