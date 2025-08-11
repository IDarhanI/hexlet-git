from more_itertools import (
    chunked as _chunked,
    sliced as _sliced,
    flatten as _flatten
)

# Реэкспортируем с удобными именами
def chunked(iterable, n):
    """Разбивает iterable на чанки по n элементов."""
    return list(_chunked(iterable, n))

def sliced(sequence, n):
    """Разбивает sequence на срезы по n элементов."""
    return list(_sliced(sequence, n))

def flatten(iterable):
    """Рекурсивно выравнивает вложенные iterable."""
    return list(_flatten(iterable))

__all__ = ["chunked", "sliced", "flatten"]  