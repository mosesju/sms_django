# Generated by Django 3.0.6 on 2020-05-09 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
