# Generated by Django 3.2.4 on 2021-06-30 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Name', models.CharField(max_length=255)),
                ('E_mail', models.CharField(max_length=255)),
                ('Confirm_mail', models.CharField(max_length=255)),
            ],
        ),
    ]
