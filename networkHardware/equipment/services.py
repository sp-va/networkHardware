import typing as t

from networkHardware.equipment.models import Equipment


def create_equipments(equipment_type: Equipment, serial_numbers: t.List[str], note: t.Optional[str] = None) -> t.List[Equipment]:
    equipments = []
    for sn in serial_numbers:
        eq = Equipment(equipment_type=equipment_type, serial_number=sn, note=note)
        eq.save()
        equipments.append(eq)
    return equipments
