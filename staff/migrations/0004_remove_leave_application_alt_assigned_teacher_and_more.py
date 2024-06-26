# Generated by Django 4.2.7 on 2024-02-07 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("staff", "0003_alter_staff_details_dl_bal_alter_staff_details_lop_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="leave_application",
            name="alt_assigned_teacher",
        ),
        migrations.RemoveField(
            model_name="leave_application",
            name="alt_class_sem",
        ),
        migrations.RemoveField(
            model_name="leave_application",
            name="alt_hour",
        ),
        migrations.RemoveField(
            model_name="leave_application",
            name="alt_linways_assigned",
        ),
        migrations.RemoveField(
            model_name="leave_application",
            name="alt_subject",
        ),
        migrations.CreateModel(
            name="AlternateArrangements",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("alt_class_sem", models.CharField(max_length=10)),
                ("alt_hour", models.IntegerField()),
                ("alt_subject", models.CharField(max_length=30)),
                ("alt_assigned_teacher", models.CharField(max_length=20)),
                ("alt_linways_assigned", models.CharField(max_length=5)),
                (
                    "employee_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="emp_id3",
                        to="staff.staff_details",
                    ),
                ),
            ],
        ),
    ]
