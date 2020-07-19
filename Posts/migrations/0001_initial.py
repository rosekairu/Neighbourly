# Generated by Django 3.0.8 on 2020-07-19 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('hood_name', models.CharField(max_length=100)),
                ('population', models.PositiveIntegerField(null=True)),
                ('user', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prof_pic', models.ImageField(blank=True, upload_to='images/')),
                ('bio', models.CharField(max_length=250, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('neighborhood', models.ForeignKey(default=2, null=True, on_delete=django.db.models.deletion.CASCADE, to='Posts.Neighborhood')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Police',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('tel', phone_field.models.PhoneField(blank=True, help_text='Police Station Phone Number', max_length=31)),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Posts.Neighborhood')),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice_title', models.CharField(max_length=100, null=True)),
                ('notice_pic', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('notice_details', models.CharField(max_length=250, null=True)),
                ('post_date', models.DateField(auto_now_add=True, null=True)),
                ('neighborhood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Posts.Neighborhood')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HealthCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('tel', phone_field.models.PhoneField(blank=True, help_text='Hospital Phone Number', max_length=31)),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Posts.Neighborhood')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bsns_name', models.CharField(max_length=250)),
                ('bsns_email', models.EmailField(max_length=100)),
                ('neighborhood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Posts.Neighborhood')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
