# Generated by Django 5.0.6 on 2024-06-13 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customsimpleuser',
            name='code',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='customsimpleuser',
            name='is_code_checked',
            field=models.BooleanField(default=False),
        ),
    ]
