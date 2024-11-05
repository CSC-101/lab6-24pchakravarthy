import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp

def index_smallest_from_books(books:list[data.Book], start:int) -> Optional[int]:
    if start >= len(books) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(books)):
        if books[idx].title < books[mindex].title:
            mindex = idx

    return mindex
# Part 1
def selection_sort_books(books : list[data.Book]) -> None:
    for idx in range(len(books) - 1):
        mindex = index_smallest_from_books(books, idx)
        tmp = books[mindex]
        books[mindex] = books[idx]
        books[idx] = tmp


# Part 2
def swap_case(looker : str) -> str:
    finalstr = ""
    for char in looker:
        if char.islower():
            finalstr += char.upper()
        elif char.isupper():
            finalstr += char.lower()
        else:
            finalstr += char
    return finalstr


# Part 3
def str_translate(newstr : str, old : str, new : str) -> str:
    finalstr = ""
    for char in newstr:
        if char == old:
            finalstr += new
        else:
            finalstr += char
    return finalstr


# Part 4
def histogram(newstr : str) -> dict:
    counter = {}
    words = newstr.split()
    for word in words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    return counter