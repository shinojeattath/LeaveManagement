# Generated by Django 4.2.7 on 2024-03-20 14:38

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("staff", "0021_alter_staff_details_email"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Pdf",
        ),
    ]
