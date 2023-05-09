from django.contrib import admin
from accounts.models import Sponsor, Stats, MyUser, Language, SupportLevel, Region, Level

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
    pass

@admin.register(SupportLevel)
class SupportLevelAdmin(admin.ModelAdmin):
    pass

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    pass

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    pass

