from django.contrib import admin
from .models import Manufacturer, Laptop, Desktop, Mobile

# Register your models here.


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    pass

@admin.register(Desktop)
class DesktopAdmin(admin.ModelAdmin):
    pass

@admin.register(Mobile)
class MobileAdmin(admin.ModelAdmin):
    pass
