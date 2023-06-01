# Generated by Django 4.2.1 on 2023-06-01 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cohort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cohort_name', models.CharField(max_length=100, unique=True, verbose_name='Cohort Name')),
                ('starting_date', models.DateField(verbose_name='When Start')),
                ('ending_date', models.DateField(verbose_name='When End')),
            ],
        ),
        migrations.CreateModel(
            name='Stack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Stack Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
            ],
        ),
    ]