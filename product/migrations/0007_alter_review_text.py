# Generated by Django 4.2.4 on 2023-09-05 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_review_buy_again'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(max_length=300),
        ),
    ]