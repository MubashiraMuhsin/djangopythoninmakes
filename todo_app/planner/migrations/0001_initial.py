# Generated by Django 4.2 on 2023-05-03 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Task_name', models.CharField(max_length=250)),
                ('priority', models.CharField(max_length=100)),
            ],
        ),
    ]