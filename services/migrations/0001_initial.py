# Generated by Django 3.2 on 2022-04-06 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('service_id', models.AutoField(primary_key=True, serialize=False)),
                ('service_name', models.CharField(max_length=20)),
                ('service_desc', models.TextField(max_length=255)),
            ],
        ),
    ]
