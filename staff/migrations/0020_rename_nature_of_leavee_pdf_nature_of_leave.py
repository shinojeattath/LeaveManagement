# Generated by Django 4.2.7 on 2024-02-16 05:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("staff", "0019_pdf_leave_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="pdf",
            old_name="nature_of_leavee",
            new_name="nature_of_leave",
        ),
    ]
