from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    worker_number = models.DecimalField(max_digits=4, decimal_places=0, null=True, blank=True)
    phone = PhoneNumberField(region='PL', null=True, blank=True)
    image = models.ImageField(upload_to='Workers_photo', null=True, blank=True,)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Case(models.Model):
    nazwa_dluznika = models.CharField(max_length=64, null=False, blank=False)
    nazwa_dluznika_cd = models.CharField(max_length=64, null=True, blank=True)
    adres_dluznika = models.CharField(max_length=64, null=False, blank=False)
    adres_dluznika_cd = models.CharField(max_length=64, null=True, blank=True)
    pesel_lub_nip_dluznika = models.CharField(max_length=11, null=False, blank=False)
    telefon_dluznika = PhoneNumberField(region='PL', null=True, blank=True)
    email_dluznika = models.EmailField(null=True, blank=True)
    nazwa_wierzyciela = models.CharField(max_length=64, null=False, blank=False)
    nazwa_wierzyciela_cd = models.CharField(max_length=64, null=True, blank=True)
    adres_wierzyciela = models.CharField(max_length=64, null=False, blank=False)
    adres_wierzyciela_cd = models.CharField(max_length=64, null=True, blank=True)
    pesel_lub_nip_wierzyciela = models.CharField(max_length=11, null=False, blank=False)
    telefon_wierzyciela = PhoneNumberField(region='PL', null=True, blank=True)
    email_wierzyciela = models.EmailField(null=True, blank=True)
    numer_konta = models.CharField(max_length=26, null=False, blank=False)
    prowadzacy_sprawe = models.ForeignKey(User, on_delete=models.CASCADE)


class Dokument(models.Model):
    nazwa = models.CharField(max_length=32, null=False, blank=False)
    numer_dokumenttu = models.CharField(max_length=32, null=False, blank=False)
    termin_splaty = models.DateField(null=False, blank=False)
    kwota = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    plik = models.FileField(upload_to='Files', null=False, blank=False)
    case = models.ForeignKey(Case, null=True, on_delete=models.SET_NULL)




