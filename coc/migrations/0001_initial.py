# Generated by Django 3.1 on 2020-08-10 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='players',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, null=True)),
                ('player_tag', models.CharField(max_length=200, null=True)),
                ('phone_no', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]