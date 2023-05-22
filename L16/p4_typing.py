# mypy

from typing import Union, Optional


def add(a: Union[int, str], b: Union[int, str]) -> Optional[Union[int, str]]:
#def add(a: int | str, b: int | str) -> int | str | None:
    return a + b

add('a', 'v')
