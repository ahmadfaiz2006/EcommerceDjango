# Generated by Django 3.0.6 on 2020-05-13 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200509_1343'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contactid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone', models.IntegerField(default=0)),
                ('desc', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
