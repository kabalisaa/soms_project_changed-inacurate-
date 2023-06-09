# Generated by Django 4.2.1 on 2023-06-09 12:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_module_name_alter_module_stack'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Assignment Title')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('documentFiles', models.FileField(blank=True, null=True, upload_to='document/course/assignment/', validators=[django.core.validators.FileExtensionValidator(['pdf', 'doc', 'ppt'])], verbose_name='Document')),
                ('cohort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='main.cohort', verbose_name='Cohort belonging')),
                ('stack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='main.stack', verbose_name='Stack belonging')),
            ],
        ),
        migrations.AlterField(
            model_name='cohort_schedule',
            name='cohort',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='main.cohort', verbose_name='Cohort Scheduled'),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=100, unique=True, verbose_name='Group Name')),
                ('cohort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='main.cohort', verbose_name='Cohort belonging')),
                ('stack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='main.stack', verbose_name='Stack belonging')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=100, unique=True, verbose_name='Assignment Grade')),
                ('comment', models.TextField(blank=True, verbose_name='Comment')),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to='main.assignment', verbose_name='Assignment')),
            ],
        ),
        migrations.CreateModel(
            name='AssignmentReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('documentFiles', models.FileField(blank=True, null=True, upload_to='document/course/assignment/', validators=[django.core.validators.FileExtensionValidator(['pdf', 'doc', 'ppt'])], verbose_name='Document')),
                ('status', models.BooleanField(default=False, verbose_name='Is Received')),
                ('createdDate', models.DateTimeField(auto_now=True)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='main.assignment', verbose_name='Assignment')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='main.group', verbose_name='Submitting Group')),
            ],
        ),
    ]
