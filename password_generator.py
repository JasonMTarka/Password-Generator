from typing import Union, Any
from random import choice, shuffle


class Password:
    """Set password generation parameters and generate passwords."""

    _STR_OR_INT = Union[str, int]

    def __init__(self,
                 lowercase: _STR_OR_INT = 1,
                 uppercase: _STR_OR_INT = 1,
                 nums: _STR_OR_INT = 1,
                 syms: _STR_OR_INT = 0,
                 min_nums: _STR_OR_INT = 2,
                 min_syms: _STR_OR_INT = 2,
                 pass_len: _STR_OR_INT = 8,
                 value: str = "") -> None:
        """Set instance variables and generate a password."""

        self.lowercase = int(lowercase)
        self.uppercase = int(uppercase)
        self.nums = int(nums)
        self.syms = int(syms)
        self.min_nums = int(min_nums)
        self.min_syms = int(min_syms)
        self.pass_len = int(pass_len)
        self.value = value
        if not self.value:
            self.generate()

    def __repr__(self) -> str:
        """Return string which can be used to instantiate this instance."""

        return (
            f"Password("
            f"lowercase={self.lowercase},"
            f"uppercase={self.uppercase},"
            f"nums={self.nums},"
            f"syms={self.syms},"
            f"min_nums={self.min_nums},"
            f"min_syms={self.min_syms},"
            f"pass_len={self.pass_len},"
            f"value={self.value})")

    def __str__(self) -> str:
        """Return password value as a string."""

        if self.value:
            return self.value
        else:
            return "Please select at least one character set."

    def __len__(self) -> int:
        """Return length of password."""

        return self.pass_len

    def __getitem__(self, position: int) -> Union[str, Any]:
        """Allow iterating over password characters."""

        return self.value[position]

    def __add__(self, other) -> str:
        """Allow adding to other Password objects, strings, or ints."""

        try:
            return self.value + other.value
        except AttributeError:
            return self.value + str(other)

    def generate(self) -> None:
        """Generate a password from instance attributes."""

        def _constructor() -> str:
            """Create empty password and append requested characters."""

            temp_password = []
            if self.nums:
                for i in range(0, self.min_nums):
                    temp_password.append(choice(NUMS))
            if self.syms:
                for i in range(0, self.min_syms):
                    temp_password.append(choice(SYMBOLS))
            shuffle(temp_password)
            while len(temp_password) > self.pass_len:
                temp_password.pop()
            while len(temp_password) < self.pass_len:
                temp_password.append(choice(source))
            shuffle(temp_password)
            return "".join(temp_password)

        source = ""
        LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
        UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        NUMS = "0123456789"
        SYMBOLS = "!@#$%^&*"

        if self.lowercase:
            source += LOWERCASE
        if self.uppercase:
            source += UPPERCASE
        if self.nums:
            source += NUMS
        if self.syms:
            source += SYMBOLS

        if source:
            self.value = _constructor()
