# Generated by Django 2.2.6 on 2020-02-05 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0002_banner_emailverifyrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='female', max_length=10),
        ),
    ]