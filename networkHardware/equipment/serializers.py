from rest_framework import serializers

from equipment.models import Equipment, EquipmentType
from equipment.utils import validate_serial_number


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ["_id", "equipment_type", "serial_number", "note"]


class CreateEquipmentSerializer(serializers.Serializer):
    equipment_type = serializers.PrimaryKeyRelatedField(queryset=EquipmentType.objects.all())
    serial_numbers = serializers.ListField(child=serializers.CharField(), write_only=True)
    note = serializers.CharField(required=False)

    def validate(self, data):
        equipment_type = data['equipment_type']
        mask = equipment_type.sn_mask
        errors = []
        valid_sn = []

        for sn in data['serial_numbers']:
            if not validate_serial_number(sn, mask):
                errors.append({'serial_number': sn, 'error': 'Invalid mask'})
                continue
            if Equipment.objects.filter(equipment_type=equipment_type, serial_number=sn).exists():
                errors.append({'serial_number': sn, 'error': 'Already exists'})
            else:
                valid_sn.append(sn)

        data['valid_serial_numbers'] = valid_sn
        data['errors'] = errors
        return data

class EquipmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentType
        fields = ["_id", "name", "serial_number_mask"]


