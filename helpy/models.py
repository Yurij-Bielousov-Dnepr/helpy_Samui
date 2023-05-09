# models.py
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from accounts.models import MyUser
from helpySamui.constants import REGION_CHOICES, LANGUAGE_CHOICES, LEVEL_CHOICES, TAG_HELP_NAME_CHOICES, \
    REVIEW_RATING_CHOICES


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



class Tag_help(models.Model):
    name = models.CharField(max_length=255, choices=TAG_HELP_NAME_CHOICES, verbose_name=_("Name"))

    class Meta:
        verbose_name = _("Tag Help")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            for choice in TAG_HELP_NAME_CHOICES:
                Tag_help.objects.get_or_create(name=choice[1])
        super().save(*args, **kwargs)



class HelpRequest(models.Model):
    user_nick = models.CharField(max_length=55, blank=False, null=False)
    category = models.ForeignKey(Tag_help, on_delete=models.CASCADE, default=1)
    problem_description = models.TextField(
        max_length=255, blank=False, null=False, default="-= =-"
    )
    district = models.ForeignKey(Region, on_delete=models.CASCADE, default=1)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, default=1)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=1)
    contacts = models.CharField(
        max_length=255, blank=False, null=False, default="12345"
    )

    def __str__(self):
        return self.problem_description[:50]


class HelpRequestLanguage(models.Model):
    help_request = models.ForeignKey(HelpRequest, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.pk:
            for choice in LANGUAGE_CHOICES:
                Language.objects.get_or_create(language=choice[0])
        super().save(*args, **kwargs)

class UserRequest(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='requests')
    helper_nickname = models.CharField(max_length=255)
    date = models.DateField()
    selected_service = models.CharField(choices=TAG_HELP_NAME_CHOICES, max_length=20)
    level_of_help = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES)
    rating = models.PositiveSmallIntegerField(choices=REVIEW_RATING_CHOICES)
    comment = models.TextField(blank=True)  # Добавляем поле comment
    district = models.CharField(max_length=20, choices=REGION_CHOICES, blank=True, default="Lamai")

    def __str__(self):
        return f"Request {self.pk}"
