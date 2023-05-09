# models.py
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
# from art_event.models import Event, Article
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from helpySamui.constants import REGION_CHOICES, LANGUAGE_CHOICES, LEVEL_CHOICES


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Создает и сохраняет пользователя с указанным email и паролем.
        """
        if not email:
            raise ValueError('Email обязателен для создания пользователя.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Создает и сохраняет суперпользователя с указанным email и паролем.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class MyUser(AbstractBaseUser, PermissionsMixin):
    social_networks = models.CharField( max_length=100, null=True, blank=True, default=None )
    email = models.EmailField(unique=True)
    userNick = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    category = models.CharField(
        max_length=255,
        choices=[("Helper", "Helper"), ("Customer", "Customer")],
        default="Customer",
    )
    district = models.ManyToManyField('Region')
    languages = models.ManyToManyField('Language')
    is_sponsor = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, blank=True)
    about_me = models.TextField(blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.userNick

    def get_short_name(self):
        return self.userNick

    @property
    def is_authenticated(self):
        return True if self.id else False

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

class Sponsor(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=55, choices=REGION_CHOICES)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            for choice in REGION_CHOICES:
                Region.objects.get_or_create(name=choice[1])
        super().save(*args, **kwargs)

class Language(models.Model):
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES)

    def __str__(self):
        return self.language

    def save(self, *args, **kwargs):
        if not self.pk:
            for choice in LANGUAGE_CHOICES:
                Language.objects.get_or_create(language=choice[1])
        super().save(*args, **kwargs)

class SupportLevel(models.Model):
    level = models.IntegerField(choices=LEVEL_CHOICES)

    def __str__(self):
        return f"Level {self.level}"

    def save(self, *args, **kwargs):
        if not self.pk:
            for choice in LEVEL_CHOICES:
                SupportLevel.objects.get_or_create(level=choice[0])
        super().save(*args, **kwargs)

class Level(models.Model):
    level = models.IntegerField(choices=LEVEL_CHOICES)

    def __str__(self):
        return f"Level {self.level}"

    def save(self, *args, **kwargs):
        if not self.pk:
            for choice in LEVEL_CHOICES:
                Level.objects.get_or_create(level=choice[0])
        super().save(*args, **kwargs)


class Stats(models.Model):
    date = models.DateField(auto_now_add=True)
    active_helpers = models.IntegerField(default=0)
    help_requests = models.IntegerField(default=0)
    online_users = models.IntegerField(default=0)
    last_activity = models.ForeignKey(
        MyUser, on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        verbose_name_plural = "Stats"

    def __str__(self):
        return f"{self.date} - Active helpers: {self.active_helpers}, Help requests: {self.help_requests}, Online users: {self.online_users}"
