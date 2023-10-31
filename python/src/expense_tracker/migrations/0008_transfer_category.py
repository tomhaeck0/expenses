# Generated by Django 4.2.6 on 2023-10-31 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_tracker', '0007_remove_transfer_currency_alter_organization_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='category',
            field=models.CharField(choices=[('food', 'Food'), ('house', 'House'), ('hobbies', 'Hobbies')], max_length=20, null=True),
        ),
    ]