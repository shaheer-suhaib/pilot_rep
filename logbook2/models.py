from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        user_id = extra_fields.pop('id', None)
        if not user_id:
            raise ValueError("You have not provided a valid ID")
        email = self.normalize_email(email)
        user = self.model(email=email, id=user_id, **extra_fields)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    id = models.IntegerField(primary_key=True)
    email = models.EmailField(blank=True, default='', unique=True)
    name = models.CharField(max_length=255, blank=True, default='')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['id']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Pilot(models.Model):
    pilot_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, to_field='id')

class Checker(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, to_field='id')

class Aircraft(models.Model):
    aircraft_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)
    tail_no = models.CharField(max_length=50,null=True, blank=True)


class FlightCategory(models.Model):
    category_id = models.AutoField(primary_key=True)

    engine =  models.CharField(max_length=50,null=True, blank=True)

    role =  models.CharField(max_length=50,null=True, blank=True)

    mission  = models.CharField(max_length=50,null=True, blank=True)


class FlightLog(models.Model):
    id = models.AutoField(primary_key=True)  # ADDING THIS solves your problem
    date = models.DateField(null=True, blank=True)
    route = models.CharField(max_length=50, null=True, blank=True)
    Additional_note = models.CharField(max_length=255, null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)

    read = models.BooleanField(null=True, blank=False, default=False)


    Pilot_in_comm = models.CharField(max_length=50,null=True, blank=True)
    Co_Pilot = models.CharField(max_length=50,null=True, blank=True)
    Take_off_time = models.DateTimeField(null=True, blank=True)
    Landing_time = models.DateTimeField(null=True, blank=True)
    Instrument_Flu =  models.CharField(max_length=50,null=True, blank=True)
    Day_night  =  models.CharField(max_length=50,null=True, blank=True)

    pilot_id = models.ForeignKey(Pilot, on_delete=models.CASCADE, to_field='pilot_id', null=True, blank=True)
    aircraft_id = models.ForeignKey(Aircraft, on_delete=models.CASCADE, to_field='aircraft_id', null=True, blank=True)
    category_id = models.ForeignKey(FlightCategory, on_delete=models.CASCADE, to_field='category_id', null=True, blank=True)

