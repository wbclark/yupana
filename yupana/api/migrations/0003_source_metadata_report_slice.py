# Generated by Django 2.2.4 on 2019-09-13 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_report_reportarchive_reportslice_reportslicearchive'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportslice',
            name='source_metadata',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='reportslicearchive',
            name='source_metadata',
            field=models.TextField(null=True),
        ),
    ]
