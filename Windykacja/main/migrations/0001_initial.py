# Generated by Django 3.0.5 on 2020-04-29 07:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa_dluznika', models.CharField(max_length=32)),
                ('nazwa_dluznika_cd', models.CharField(max_length=32)),
                ('adres_dluznika', models.CharField(max_length=32)),
                ('adres_dluznika_cd', models.CharField(max_length=32)),
                ('telefon_dluznika', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='PL')),
                ('email_dluznika', models.EmailField(max_length=254)),
                ('nazwa_wierzyciela', models.CharField(max_length=32)),
                ('nazwa_wierzyciela_cd', models.CharField(max_length=32)),
                ('adres_wierzyciela', models.CharField(max_length=32)),
                ('adres_wierzyciela_cd', models.CharField(max_length=32)),
                ('pesel_lub_nip_dluznika', models.CharField(max_length=11)),
                ('telefon_wierzyciela', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='PL')),
                ('email_wierzyciela', models.EmailField(max_length=254)),
                ('numer_konta', models.CharField(max_length=32)),
                ('prowadzacy_sprawe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worker_number', models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='PL')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Workers_photo')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dokument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=32)),
                ('numer_dokumenttu', models.CharField(max_length=32)),
                ('termin_splaty', models.DateField()),
                ('kwota', models.DecimalField(decimal_places=2, max_digits=6)),
                ('plik', models.FileField(upload_to='')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Case')),
            ],
        ),
    ]