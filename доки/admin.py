from django.contrib import admin
from reviews.models import Review, Re_view
from offer.models import Helper
from helpy.models import Tag_help, HelpRequest, HelpRequestLanguage
from art_event.models import Article, Event
from accounts.models import (
    Sponsor,
    Stats,
    MyUser,
    Language,
    SupportLevel,
    Region,
    Level,
    Favorites,
)
#
# admin.site.register(Favorites)
# admin.site.register(MyUser)
# admin.site.register(Article)
# admin.site.register(Event)
# admin.site.register(Helper)
# admin.site.register(Review)
# admin.site.register(Tag_help)
# admin.site.register(Sponsor)
# admin.site.register(Re_view)
# admin.site.register(Stats)

@admin.register(Favorites)
class FavoritesAdmin(admin.ModelAdmin):
    pass

@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    pass

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass

@admin.register(Helper)
class HelperAdmin(admin.ModelAdmin):
    pass

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag_help)
class Tag_helpAdmin(admin.ModelAdmin):
    pass

@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    pass

@admin.register(Re_view)
class Re_viewAdmin(admin.ModelAdmin):
    pass

@admin.register(Stats)
class StatsAdmin(admin.ModelAdmin):
    pass

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass

@admin.register(SupportLevel)
class SupportLevelAdmin(admin.ModelAdmin):
    pass

@admin.register(HelpRequest)
class HelpRequestAdmin(admin.ModelAdmin):
    pass

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    pass

@admin.register(HelpRequestLanguage)
class HelpRequestLanguageAdmin(admin.ModelAdmin):
    pass

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    pass

@admin.register(Language, SupportLevel, HelpRequest, Region, HelpRequestLanguage, Level)
class HiddenAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False
