# def print_even_odd(arr):
#     # Printing even numbers
#     for num in arr:
#         if num % 2 == 0:
#             print("List of even numbers:", end=" ")
#             print(num, end=",")
#     print()  # For a new line after printing all even numbers
#
#     # Printing odd numbers
#     for num in arr:
#         if num % 2 != 0:
#             print("List of odd numbers:", end=" ")
#             print(num, end=",")
#
#
# if __name__ == "__main__":
#     arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     print_even_odd(arr)


def print_even_odd(arr):
    even_numbers = []
    odd_numbers = []

    # Collecting even and odd numbers
    for num in arr:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    # Printing the collected even and odd numbers
    print("List of even numbers:", ", ".join(map(str, even_numbers)))
    print("List of odd numbers:", ", ".join(map(str, odd_numbers)))


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print_even_odd(arr)

