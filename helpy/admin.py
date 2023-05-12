from django.contrib import admin
from helpy.models import Tag_help, HelpRequest, HelpRequestLanguage


class Tag_helpAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_name_display']


admin.site.register(Tag_help, Tag_helpAdmin)

@admin.register(HelpRequest)
class HelpRequestAdmin(admin.ModelAdmin):
    pass


@admin.register(HelpRequestLanguage)
class HiddenAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False
