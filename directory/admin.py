from django.contrib import admin

# Register your models here.
from .models import Folder
from .models import File

admin.site.register(Folder)
admin.site.register(File)
