from django.contrib import admin
from hvad.admin import TranslatableAdmin
from cockpit.models import Page


class PageAdmin(TranslatableAdmin):
    class Meta:
        model = Page

    #
    # Workaround for prepopulated_fields and fieldsets from here:
    # https://github.com/KristianOellegaard/django-hvad/issues/10#issuecomment-5572524
    #
    def __init__(self, *args, **kwargs):
        super(PageAdmin, self).__init__(*args, **kwargs)
        self.prepopulated_fields = {'slug': ('heading',)}

    list_display = ('__str__', 'all_translations', 'created_at', 'parent')
    list_filter = ['created_at']
    search_fields = ['translations__heading']
    date_hierarchy = 'created_at'

    def changelist_view(self, request, extra_context=None):

        return super(PageAdmin, self).changelist_view(request, extra_context)



admin.site.register(Page, PageAdmin)