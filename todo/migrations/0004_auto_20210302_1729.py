# Generated by Django 3.1.3 on 2021-03-02 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_task_dateandtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='dateandtime',
            field=models.CharField(max_length=50),
        ),
    ]
