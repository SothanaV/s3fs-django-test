from django.contrib import admin
from .models import Upload
# Register your models here.

class UploadAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Upload._meta.fields]
admin.site.register(Upload, UploadAdmin)
