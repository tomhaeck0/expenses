# Generated by Django 4.2.6 on 2023-10-31 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_tracker', '0006_remove_transfer_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transfer',
            name='currency',
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
