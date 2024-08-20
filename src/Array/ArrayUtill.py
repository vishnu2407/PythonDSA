import random


def reverse(arr):
    return arr[::-1]


def concat(arr1, arr2):
    return arr1 + arr2


def shuffle(arr):
    shuffled = arr[:]  # Create a copy of the original array
    random.shuffle(shuffled)
    return shuffled

def sort_ascending(arr):
    return sorted(arr)

def sort_descending(arr):
    return sorted(arr, reverse=True)


if __name__ == "__main__":
    arr = [2, 5, 4, 1, 3, 6, 7, 8, 9, 10]

    reversed_arr = reverse(arr)
    concatenated_arr = concat(arr, reversed_arr)
    shuffled_arr = shuffle(arr)
    ascending_arr = sort_ascending(arr)
    descending_arr = sort_descending(arr)

    print("Original array:", arr)
    print("Reversed array:", reversed_arr)
    print("Concatenated array:", concatenated_arr)
    print("Shuffled array:", shuffled_arr)
    print("Ascending order:", ascending_arr)
    print("Descending order:", descending_arr)

    #Output:
    # Original array: [2, 5, 4, 1, 3, 6, 7, 8, 9, 10]
    # Reversed array: [10, 9, 8, 7, 6, 3, 1, 4, 5, 2]
    # Concatenated array: [2, 5, 4, 1, 3, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 3, 1, 4, 5, 2]
    # Shuffled array: [1, 3, 4, 2, 5, 6, 7, 8, 9, 10]
    # Ascending order: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Descending order: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]