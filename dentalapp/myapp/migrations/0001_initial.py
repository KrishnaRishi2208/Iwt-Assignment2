# Generated by Django 4.0.5 on 2022-07-03 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=30)),
                ('LastName', models.CharField(max_length=30)),
                ('Email', models.CharField(blank=b'I01\n', max_length=60)),
                ('City', models.CharField(blank=b'I01\n', max_length=30)),
                ('PreviousProcedures', models.CharField(blank=b'I01\n', max_length=300)),
            ],
        ),
    ]