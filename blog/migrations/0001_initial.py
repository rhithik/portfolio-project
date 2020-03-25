# Generated by Django 2.2.11 on 2020-03-24 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('pub_date', models.DateField()),
                ('body', models.CharField(max_length=5000)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
