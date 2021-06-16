from typing import Union, Any
from random import choice, shuffle


class Password:

    _STR_OR_INT = Union[str, int]

    def __init__(self, lowercase: _STR_OR_INT = 1, uppercase: _STR_OR_INT = 1, nums: _STR_OR_INT = 1, syms: _STR_OR_INT = 0,
                 min_nums: _STR_OR_INT = 2, min_syms: _STR_OR_INT = 2, pass_len: _STR_OR_INT = 8, value: str = "") -> None:
        self.nums = int(nums)
        self.syms = int(syms)
        self.lowercase = int(lowercase)
        self.uppercase = int(uppercase)
        self.min_nums = int(min_nums)
        self.min_syms = int(min_syms)
        self.pass_len = int(pass_len)
        self.value = value
        if not self.value:
            self.generate()

    def __repr__(self) -> str:
        return f"""Password(lowercase={self.lowercase}, uppercase={self.uppercase}, nums={self.nums}, syms={self.syms},
                 min_nums={self.min_nums}, min_syms={self.min_syms}, pass_len={self.pass_len}, value={self.value})"""

    def __str__(self) -> str:
        if self.value:
            return self.value
        else:
            return "Please select at least one character set."

    def __len__(self) -> int:
        return self.pass_len

    def __getitem__(self, position: int) -> Union[str, Any]:
        return self.value[position]

    def __add__(self, other) -> str:
        try:
            return self.value + other.value
        except AttributeError as e:
            return f"AttributeError: {other} has no attribute {e}!"

    def generate(self) -> None:

        def _constructor() -> str:
            temp_password = []
            if self.nums:
                for i in range(0, self.min_nums):
                    temp_password.append(choice(NUMS))
            if self.syms:
                for i in range(0, self.min_syms):
                    temp_password.append(choice(SYMBOLS))
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
