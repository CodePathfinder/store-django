# Generated by Django 3.1 on 2021-06-09 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
