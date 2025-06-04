from django.contrib import admin

from .models import Equipment, EquipmentType


admin.site.register((Equipment, EquipmentType))
