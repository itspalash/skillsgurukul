# Generated by Django 3.0 on 2022-01-06 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updates',
            name='email',
            field=models.CharField(max_length=120, verbose_name='email'),
        ),
    ]