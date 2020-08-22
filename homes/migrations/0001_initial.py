# Generated by Django 3.0.8 on 2020-07-31 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='credentials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'homepage',
            },
        ),
    ]
