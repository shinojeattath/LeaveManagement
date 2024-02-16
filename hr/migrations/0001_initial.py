# Generated by Django 4.2.7 on 2024-02-15 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("staff", "0015_remove_alternatearrangements_submitted_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Leave_Application_hr",
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
                ("name", models.CharField(max_length=20)),
                ("department", models.CharField(max_length=5)),
                ("nature_of_leave", models.CharField(max_length=20)),
                ("no_of_days", models.IntegerField(null=True)),
                ("leave_from", models.DateField()),
                ("reason", models.CharField(max_length=200)),
                (
                    "status_of_request",
                    models.CharField(default="PENDING", max_length=10),
                ),
                ("time_of_request", models.DateTimeField(null=True)),
                ("alt_linways_assigned", models.CharField(max_length=5, null=True)),
                ("submitted", models.BooleanField(default=False)),
                ("certificate", models.FileField(upload_to="media/")),
                (
                    "employee_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="emp_id4",
                        to="staff.staff_details",
                    ),
                ),
            ],
        ),
    ]