# Generated by Django 4.1 on 2022-11-10 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('usn', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('sem', models.CharField(default='', max_length=50)),
                ('mobile_no', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
