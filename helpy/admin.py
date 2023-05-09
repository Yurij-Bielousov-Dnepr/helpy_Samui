from django.contrib import admin
from helpy.models import Tag_help, HelpRequest, HelpRequestLanguage


@admin.register(Tag_help)
class Tag_helpAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(HelpRequest)
class HelpRequestAdmin(admin.ModelAdmin):
    pass


@admin.register(HelpRequestLanguage)
class HiddenAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False
