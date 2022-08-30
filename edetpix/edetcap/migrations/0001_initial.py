# Generated by Django 4.0.6 on 2022-08-25 16:01

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('staff_id', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=6)),
                ('blood_group', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], max_length=3)),
                ('category', models.CharField(choices=[('University Staff', 'University Staff'), ('Ventures Staff', 'Ventures Staff'), ('Undergrad', 'Undergrad'), ('Postgrad', 'Postgrad')], max_length=30)),
                ('passport', models.ImageField(help_text='White background', upload_to='user/passport')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_session', models.CharField(choices=[('2019/2020', '2019/2020'), ('2020/2021', '2020/2021'), ('2021/2022', '2021/2022'), ('2022/2023', '2022/2023'), ('2023/2024', '2023/2024'), ('2024/2025', '2024/2025'), ('2025/2026', '2025/2026'), ('2026/2027', '2026/2027'), ('2027/2028', '2027/2028'), ('2028/2029', '2028/2029'), ('2029/2030', '2029/2030'), ('2030/2031', '2030/2031'), ('2031/2032', '2031/2032'), ('2032/2033', '2032/2033'), ('2033/2034', '2033/2034'), ('2034/2035', '2034/2035'), ('2035/2036', '2035/2036'), ('2036/2037', '2036/2037'), ('2037/2038', '2037/2038'), ('2038/2039', '2038/2039'), ('2039/2040', '2039/2040'), ('2040/2041', '2040/2041'), ('2041/2042', '2041/2042'), ('2042/2043', '2042/2043'), ('2043/2044', '2043/2044'), ('2044/2045', '2044/2045'), ('2045/2046', '2045/2046'), ('2046/2047', '2046/2047'), ('2047/2048', '2047/2048'), ('2048/2049', '2048/2049'), ('2049/2050', '2049/2050'), ('2050/2051', '2050/2051'), ('2051/2052', '2051/2052'), ('2052/2053', '2052/2053'), ('2053/2054', '2053/2054'), ('2054/2055', '2054/2055'), ('2055/2056', '2055/2056'), ('2056/2057', '2056/2057'), ('2057/2058', '2057/2058'), ('2058/2059', '2058/2059'), ('2059/2060', '2059/2060'), ('2060/2061', '2060/2061'), ('2061/2062', '2061/2062'), ('2062/2063', '2062/2063'), ('2063/2064', '2063/2064'), ('2064/2065', '2064/2065'), ('2065/2066', '2065/2066'), ('2066/2067', '2066/2067'), ('2067/2068', '2067/2068'), ('2068/2069', '2068/2069'), ('2069/2070', '2069/2070')], max_length=50)),
            ],
            options={
                'verbose_name': 'Session',
                'verbose_name_plural': 'Sessions',
                'ordering': ['academic_session'],
            },
        ),
        migrations.CreateModel(
            name='UniversityStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=6)),
                ('designation', models.CharField(help_text='As written in appointment letter', max_length=50)),
                ('blood_group', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], max_length=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('fellow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edetcap.session')),
            ],
            options={
                'verbose_name': 'UniversityStaff',
                'verbose_name_plural': 'Universities',
                'ordering': ['-created_at'],
            },
        ),
    ]
