# Generated by Django 3.2.25 on 2024-07-29 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='imgfile',
        ),
        migrations.AddField(
            model_name='product',
            name='imgfiletest',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
