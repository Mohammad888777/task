from django.contrib import admin

from .models import User,Code
from import_export.admin import ImportExportModelAdmin


class UserAdmin(ImportExportModelAdmin):

    list_display=[
        "id",
        "phone"
    ]


admin.site.register(
    User,UserAdmin
)
admin.site.register([
    Code
])

