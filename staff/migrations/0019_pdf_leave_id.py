# Generated by Django 4.2.7 on 2024-02-16 05:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("staff", "0018_rename_name_pdf_employee_id_pdf_nature_of_leavee"),
    ]

    operations = [
        migrations.AddField(
            model_name="pdf",
            name="leave_id",
            field=models.IntegerField(null=True),
        ),
    ]
