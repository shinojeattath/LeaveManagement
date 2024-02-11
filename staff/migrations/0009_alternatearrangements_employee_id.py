# Generated by Django 4.2.7 on 2024-02-07 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("staff", "0008_remove_alternatearrangements_alt_class_sem_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="alternatearrangements",
            name="employee_id",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="emp_id3",
                to="staff.staff_details",
            ),
            preserve_default=False,
        ),
    ]