"""Search algorithms used in Lab10.

Contains sequential and binary search implementations with optional step counting.
"""

from __future__ import annotations

from typing import Any, Iterable, Tuple


def sequential_search(a_list: Iterable[Any], target: Any) -> bool:
    """Return True if ``target`` is present in ``a_list`` using linear scan.

    This is the simplest search algorithm. If the list is empty or the target
    is not found the function returns ``False``.
    """

    for item in a_list:
        if item == target:
            return True
    return False


def binary_search(a_list: list[Any], target: Any) -> bool:
    """Perform binary search on a **sorted** list.

    The function returns ``True`` if ``target`` exists in ``a_list`` and
    ``False`` otherwise. The list **must** be sorted in ascending order or
    the behavior is undefined.
    """

    low = 0
    high = len(a_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if a_list[mid] == target:
            return True
        elif a_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


def sequential_search_counted(
    a_list: Iterable[Any], target: Any
) -> Tuple[bool, int]:
    """Like :func:`sequential_search` but also return the number of comparisons.

    The returned count is the number of elements examined before the search
    terminated. When the list is empty the count is zero.
    """

    count = 0
    for item in a_list:
        count += 1
        if item == target:
            return True, count
    return False, count


def binary_search_counted(a_list: list[Any], target: Any) -> Tuple[bool, int]:
    """Binary search variant that counts comparisons.

    The returned tuple contains ``(found, comparisons)``. ``comparisons`` is
    the number of times an element was inspected.
    """

    low = 0
    high = len(a_list) - 1
    count = 0

    while low <= high:
        mid = (low + high) // 2
        count += 1
        if a_list[mid] == target:
            return True, count
        elif a_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False, count
