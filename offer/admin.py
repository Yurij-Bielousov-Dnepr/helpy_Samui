from django.contrib import admin
from offer.models import Helper

@admin.register(Helper, site=admin.site)
class HelperAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'display_support_levels', 'display_regions', 'display_languages')
    list_filter = ('support_levels', 'regions', 'languages')
    search_fields = ('name',)

    def display_support_levels(self, obj):
        return ', '.join(str(level) for level in obj.support_levels.all())

    def display_regions(self, obj):
        return ', '.join(str(region) for region in obj.regions.all())

    def display_languages(self, obj):
        return ', '.join(str(language) for language in obj.languages.all())

    display_support_levels.short_description = 'Support Levels'

    display_regions.short_description = 'Regions'

    display_languages.short_description = 'Languages'
