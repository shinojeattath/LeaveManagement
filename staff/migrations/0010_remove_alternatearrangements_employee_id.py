# Generated by Django 4.2.7 on 2024-02-07 20:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("staff", "0009_alternatearrangements_employee_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="alternatearrangements",
            name="employee_id",
        ),
    ]