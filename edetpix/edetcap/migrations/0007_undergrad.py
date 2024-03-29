# Generated by Django 4.0.6 on 2022-09-06 10:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edetcap', '0006_universitystaff_passport'),
    ]

    operations = [
        migrations.CreateModel(
            name='Undergrad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matric_id', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=6)),
                ('level', models.CharField(choices=[('100', '100'), ('200', '200'), ('300', '300'), ('400', '400'), ('500', '500')], max_length=10)),
                ('blood_group', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], max_length=3)),
                ('department', models.CharField(choices=[('Mass Comm', 'Mass Comm'), ('Law', 'Law'), ('Bio-Chem', 'Bio-Chem'), ('Civil-Eng', 'Civil-Eng'), ('Nursing', 'Nursing')], default='Nursing', max_length=20)),
                ('passport', models.ImageField(upload_to='undergrad/passport')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('fellow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edetcap.session')),
            ],
            options={
                'verbose_name': 'Undergrad',
                'verbose_name_plural': 'Undergrads',
                'ordering': ['-created_at'],
            },
        ),
    ]
