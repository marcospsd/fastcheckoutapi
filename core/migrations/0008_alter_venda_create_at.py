# Generated by Django 4.0.2 on 2022-04-28 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_corpo_venda_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='create_at',
            field=models.DateField(auto_now=True),
        ),
    ]
