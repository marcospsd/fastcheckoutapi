# Generated by Django 4.0.2 on 2022-05-03 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_corpo_venda_hour_at_formapagamento_hour_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nome',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='venda',
            name='nome',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
