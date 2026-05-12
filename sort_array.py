"""
Python code to sort an array (list) in various ways
"""

# Example 1: Sort a list using the built-in sorted() function
def sort_array_sorted(arr):
    """
    Sort an array using sorted() - returns a new sorted list
    """
    return sorted(arr)


# Example 2: Sort a list in-place using the .sort() method
def sort_array_in_place(arr):
    """
    Sort an array in-place using .sort() method
    """
    arr.sort()
    return arr


# Example 3: Sort in descending order
def sort_array_descending(arr):
    """
    Sort an array in descending order
    """
    return sorted(arr, reverse=True)


# Example 4: Custom sorting with key function
def sort_array_custom(arr, key_func=None):
    """
    Sort an array with a custom key function
    """
    return sorted(arr, key=key_func)


if __name__ == "__main__":
    # Sample array
    numbers = [64, 34, 25, 12, 22, 11, 90]

    print("Original array:", numbers)
    print("Sorted (ascending):", sort_array_sorted(numbers))
    print("Sorted (descending):", sort_array_descending(numbers))

    # Example with strings
    fruits = ["banana", "apple", "cherry", "date"]
    print("\nOriginal fruits:", fruits)
    print("Sorted fruits:", sort_array_sorted(fruits))

    # Example with custom key - sort by length
    print("Sorted by length:", sort_array_custom(fruits, key=len))
