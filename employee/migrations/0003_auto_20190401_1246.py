# Generated by Django 2.1.7 on 2019-04-01 12:46

from django.db import migrations, models
import django.db.models.deletion
import employee.models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_educationrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecordImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('cnic', 'CNIC'), ('domicile', 'Domicile'), ('metric', 'Metric Certificate'), ('intermediate', 'Intermediate Certificate'), ('graduation', 'Graduation Certificate'), ('other', 'Other Documents')], max_length=15)),
                ('image', models.ImageField(upload_to=employee.models.employee_certificates_path, verbose_name='Document Photo')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee')),
            ],
        ),
        migrations.RemoveField(
            model_name='educationrecord',
            name='certificate_image',
        ),
    ]
