import random


def quicksort(lst: list[int]) -> None:
    def _quicksort(start: int, end: int) -> None:
        if start >= end:
            return
        else:
            pivot = start
            i1 = start + 1
            i2 = end
            while i1 <= i2:
                if lst[i1] > lst[pivot] > lst[i2]:
                    lst[i1], lst[i2] = lst[i2], lst[i1]
                elif lst[i1] <= lst[pivot]:
                    i1 += 1
                elif lst[pivot] <= lst[i2]:
                    i2 -= 1
            print(i1, i2, pivot)
            lst[i1 - 1], lst[pivot] = lst[pivot], lst[i1 - 1]
            _quicksort(start, i1 - 1)
            _quicksort(i1 + 1, end)

    _quicksort(0, len(lst) - 1)


# a = [9, 9, 9, 5, 4, 4, 4]
# quicksort(a)
# print(a)

def mergesort(lst: list[int]) -> None:
    pass


def insertion_sort(lst: list[int]) -> None:
    for i in range(0, len(lst)):
        while i > 0 and lst[i - 1] > lst[i]:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            i -= 1


def selection_sort(lst: list[int]) -> None:
    for i in range(0, len(lst) - 1):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]


def test_sort():
    sort_to_test = insertion_sort
    n = 1000
    for _ in range(n):
        test_list = get_random_list(50)
        test_list_copy = sorted(test_list)
        sort_to_test(test_list)
        if test_list_copy != test_list:
            print(f"Expected: {test_list_copy}\nGot: {test_list}")
            return
        print("passed")



def _in_place_quicksort(lst: list, b: int, e: int) -> None:
    if e - b < 2:
        pass
    else:
        pivot_index = _in_place_partition_indexed(lst, b, e)
        print(b, pivot_index, e)
        _in_place_quicksort(lst, b, pivot_index)
        _in_place_quicksort(lst, pivot_index + 1, e)


def _in_place_partition_indexed(lst: list, b: int, e: int) -> int:
    pivot = lst[b]
    small_i = b + 1
    big_i = e
    while small_i < big_i:
        if lst[small_i] <= pivot:
            small_i += 1
        else:
            lst[small_i], lst[big_i - 1] = lst[big_i - 1], lst[small_i]
            big_i -= 1
    lst[b], lst[small_i - 1] = lst[small_i - 1], lst[b]
    return small_i - 1


def get_random_list(n: int) -> list[int]:
    return [
        random.randint(0, 100) for _ in range(0, n)
    ]

test_sort()