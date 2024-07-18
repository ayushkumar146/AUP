# Generated by Django 5.0.7 on 2024-07-18 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submit', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codesubmission',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='codesubmission',
            name='desired_output',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='codesubmission',
            name='language',
            field=models.CharField(max_length=10),
        ),
    ]
