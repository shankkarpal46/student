# Generated by Django 5.1.2 on 2024-11-10 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('student_image', models.ImageField(upload_to='students/')),
                ('student_first_name', models.CharField(max_length=100)),
                ('student_middle_name', models.CharField(max_length=100)),
                ('student_last_name', models.CharField(max_length=100)),
                ('student_date_birth', models.DateField()),
                ('student_address', models.TextField(default='Please enter your address.')),
                ('student_email', models.EmailField(max_length=254)),
                ('student_contact_number', models.PositiveBigIntegerField()),
                ('student_course', models.CharField(max_length=100)),
            ],
        ),
    ]