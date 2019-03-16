"""
PRIVATE MODULE: do not import (from) it directly.

This module contains functionality for supporting the compatibility of jsons
with multiple Python versions.
"""
from enum import Enum


class Flag(Enum):
    """
    This is a light version of the Flag enum type that was introduced in
    Python3.6. It supports the use of pipes for members (Flag.A | Flag.B).
    """

    @classmethod
    def _get_inst(cls, value):
        try:
            result = cls(value)
        except ValueError:
            pseudo_member = object.__new__(cls)
            pseudo_member._value_ = value
            contained = [elem.name for elem in cls if elem in pseudo_member]
            pseudo_member._name_ = '|'.join(contained)
            result = pseudo_member
        return result

    def __or__(self, other: 'Flag') -> 'Flag':
        new_value = other.value | self.value
        return self._get_inst(new_value)

    def __contains__(self, item: 'Flag') -> bool:
        return item.value == self.value & item.value

    __ror__ = __or__
