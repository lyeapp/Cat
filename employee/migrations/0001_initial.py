# Generated by Django 4.0.3 on 2022-03-25 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeid', models.IntegerField()),
                ('employeename', models.CharField(max_length=255)),
                ('employeeemail', models.CharField(max_length=255)),
                ('employeecontact', models.IntegerField()),
                ('employeedob', models.CharField(max_length=50)),
            ],
        ),
    ]