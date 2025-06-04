import re

from constants import MASK_TO_REGEX_MAPPING


def validate_serial_number(mask: str, number: str) -> bool:
    regex_pattern = ""

    for ch in mask:
        regex_pattern += MASK_TO_REGEX_MAPPING[ch]

    return re.fullmatch(
        pattern=regex_pattern,
        string=number
    ) is not None
