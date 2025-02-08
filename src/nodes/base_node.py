from abc import ABC, abstractmethod
from typing import Any

class BaseNode(ABC):
    """
    Abstract base class for all tree nodes.
    """
    def __init__(self, value: Any) -> None:
        self._value = value

    @property
    def value(self) -> Any:
        return self._value

    @value.setter
    def value(self, value: Any) -> None:
        self._value = value

    @abstractmethod
    def __str__(self) -> str:
        """Return a string representation of the node."""
        pass

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BaseNode):
            return NotImplemented
        try:
            # print(int(self._value) , int(other.value))
            return int(self._value) == int(other.value)
        except (ValueError, TypeError):
            raise TypeError("Node values must be comparable as integers.")

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, BaseNode):
            return NotImplemented
        try:
            return int(self._value) < int(other.value)
        except (ValueError, TypeError):
            raise TypeError("Node values must be comparable as integers.")
