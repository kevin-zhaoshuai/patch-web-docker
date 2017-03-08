from django.contrib import admin
from commitinfo.models import Kernel_Project

class CommitInfoAdmin(admin.ModelAdmin):
    # ...
    list_display = ('name', 'email','datetime','comment','hashvalue')

admin.site.register(Kernel_Project,CommitInfoAdmin)
