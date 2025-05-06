from __future__ import annotations
from typing import Any, Generator


class Dictionary:
    def __init__(self) -> None:
        self._items = []

    def __getitem__(self, key: Any) -> Any:
        for k, v in self._items:
            if k == key:
                return v
        raise KeyError(key)

    def __setitem__(self, key: Any, value: Any) -> None:
        for i, (k, _) in enumerate(self._items):
            if k == key:
                self._items[i] = (key, value)
                return
        self._items.append((key, value))

    def __delitem__(self, key: Any) -> None:
        for i, (k, _) in enumerate(self._items):
            if k == key:
                del self._items[i]
                return
        raise KeyError(key)

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Generator:
        return (k for k, _ in self._items)

    def get(self, key: Any) -> Any | None:
        for k, v in self._items:
            if k == key:
                return v
        return None

    def pop(self, key: Any) -> Any:
        for i, (k, v) in enumerate(self._items):
            if k == key:
                del self._items[i]
                return v
        raise KeyError(key)

    def update(self, key: Any, value: Any) -> Dictionary:
        self[key] = value
        return self

    def clear(self) -> None:
        self._items.clear()

    def get_capacity(self) -> int:
        capacity = 8
        length = len(self)
        while length >= capacity - 3:
            capacity *= 2
        return capacity
