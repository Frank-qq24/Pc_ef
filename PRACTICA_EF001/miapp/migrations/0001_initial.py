# Generated by Django 4.0.6 on 2022-08-03 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idcourse', models.TextField(max_length=10)),
                ('code', models.TextField(max_length=8)),
                ('name', models.TextField()),
                ('hour', models.TextField()),
                ('credits', models.TextField()),
                ('state', models.CharField(max_length=1)),
            ],
        ),
    ]
