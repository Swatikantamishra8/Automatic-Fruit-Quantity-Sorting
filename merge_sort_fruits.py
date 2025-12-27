#!/usr/bin/env python3
"""
merge_sort_fruits.py
Run: python3 merge_sort_fruits.py
"""

from dataclasses import dataclass
from typing import List


@dataclass
class Fruit:
    name: str
    quantity: int


def merge(arr: List[Fruit], left: int, mid: int, right: int) -> None:
    """
    Merge two sorted subarrays arr[left:mid+1] and arr[mid+1:right+1]
    Stable merge: if quantities are equal, left element is chosen first
    """
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        if left_part[i].quantity <= right_part[j].quantity:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    # Copy remaining elements
    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1


def merge_sort(arr: List[Fruit], left: int, right: int) -> None:
    if left < right:
        mid = left + (right - left) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)


def main() -> None:
    try:
        n = int(input("Enter number of fruit entries: ").strip())
        if n <= 0:
            raise ValueError
    except ValueError:
        print("Invalid number of entries.")
        return

    fruits: List[Fruit] = []

    print("Enter fruit entries as: <Name> <Quantity>")
    print("Example: Apple 12")

    i = 0
    while i < n:
        line = input(f"Entry {i + 1}: ").strip()
        parts = line.split()

        if len(parts) != 2:
            print("Invalid format. Please provide: Name Quantity")
            continue

        name, qty_str = parts
        try:
            quantity = int(qty_str)
        except ValueError:
            print("Quantity must be an integer.")
            continue

        fruits.append(Fruit(name=name, quantity=quantity))
        i += 1

    merge_sort(fruits, 0, len(fruits) - 1)

    print("\nSorted fruit list by quantity (ascending):")
    print("------------------------------------------")
    for fruit in fruits:
        print(f"{fruit.name:<20} {fruit.quantity:>10}")


if __name__ == "__main__":
    main()
