# Generated by Django 4.2.7 on 2024-02-16 05:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("staff", "0017_pdf_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="pdf",
            old_name="name",
            new_name="employee_id",
        ),
        migrations.AddField(
            model_name="pdf",
            name="nature_of_leavee",
            field=models.CharField(max_length=10, null=True),
        ),
    ]
