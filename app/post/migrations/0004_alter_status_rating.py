# Generated by Django 3.2 on 2023-02-09 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_status_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='rating',
            field=models.IntegerField(blank=True, choices=[(None, 'None'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None, null=True),
        ),
    ]
