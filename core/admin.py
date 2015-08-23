from django.contrib import admin
import core.models as coremodels
# Register your models here.

admin.site.register(coremodels.Workplace)
admin.site.register(coremodels.Review)