from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Vendor
from .resources import VendorResource
class VendorAdmin(ImportExportModelAdmin):
    resource_class = VendorResource


# Register your models here.
admin.site.register(Vendor, VendorAdmin)
