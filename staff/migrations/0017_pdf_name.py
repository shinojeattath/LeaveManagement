# Generated by Django 4.2.7 on 2024-02-15 10:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("staff", "0016_pdf"),
    ]

    operations = [
        migrations.AddField(
            model_name="pdf",
            name="name",
            field=models.CharField(max_length=10, null=True),
        ),
    ]
