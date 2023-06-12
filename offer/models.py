# models.py
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

import accounts
from accounts.models import SupportLevel, Region, Language
from helpy.models import Tag_help


class Helper(accounts.MyUser):
    name = models.CharField(max_length=255)
    vip = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag_help)
    support_levels = models.ManyToManyField(SupportLevel)
    regions = models.ManyToManyField(Region)
    contacts = models.TextField()
    user_offer_is_free = models.BooleanField(default=False)
    soft_skills = models.TextField(blank=True, null=True)
