# Generated by Django 2.2.5 on 2020-04-24 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Politician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house', models.CharField(max_length=30)),
                ('state_or_district', models.CharField(blank=True, max_length=20)),
                ('party', models.CharField(choices=[('Democrat', 'Democrat'), ('Republican', 'Republican'), ('Other', 'Other')], max_length=20)),
                ('positions', models.CharField(max_length=20)),
                ('year_elected', models.PositiveIntegerField(blank=True)),
            ],
        ),
    ]
