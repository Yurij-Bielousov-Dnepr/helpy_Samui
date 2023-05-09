from django.contrib import admin
from offer.models import Helper

@admin.register(Helper)
class HelperAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', "support_levels", "regions", "languages")

    def support_levels(self, obj):
        return obj.support_levels_name

    def regions(self, obj):
        return obj.regions_name

    def languages(self, obj):
        return obj.languages_name
    support_levels.short_description = 'support_levels'
    regions.short_description = 'regions'
    languages.short_description = 'languages'