from django.contrib import admin
from accounts.models import Sponsor, Stats, MyUser, Language, SupportLevel, Region, Level
from helpySamui.constants import LEVEL_CHOICES, REGION_CHOICES


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    pass


@admin.register(Stats)
class StatsAdmin(admin.ModelAdmin):
    pass


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    pass


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'get_name_display')

    @staticmethod
    def get_name_display(obj):
        return obj.language


@admin.register(SupportLevel)
class SupportLevelAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'get_name_display')

    @staticmethod
    def get_name_display(obj):
        return dict(LEVEL_CHOICES).get(obj.level)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'get_region_display')

    @staticmethod
    def get_region_display(obj):
        return dict(REGION_CHOICES).get(obj.region)


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'get_level_display')

    @staticmethod
    def get_level_display(obj):
        return dict(LEVEL_CHOICES).get(obj.level)