# Generated by Django 3.2 on 2021-04-18 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20210406_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default=0, max_length=10, verbose_name='password'),
            preserve_default=False,
        ),
    ]
