from django.db import models
from uuid import uuid4

from equipment.constants import SERIAL_NUMBER_MAX_LENGTH


class EquipmentType(models.Model):
    _id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    name = models.CharField(
        max_length=50,
        unique=True
    )
    serial_number_mask = models.CharField(
        max_length=SERIAL_NUMBER_MAX_LENGTH,
        unique=True
    )


class Equipment(models.Model):
    _id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    equipment_type = models.ForeignKey(
        EquipmentType,
        on_delete=models.CASCADE
    )
    serial_number = models.CharField(
        max_length=SERIAL_NUMBER_MAX_LENGTH,
        unique=True
    )
    note = models.CharField(
        max_length=255,
        blank=True
    )
    is_deleted = models.BooleanField(
        default=False
    )
