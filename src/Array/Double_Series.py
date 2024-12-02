import math

def double_series(arr):
    return [num * 2 for num in arr]
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #n = int(input("Enter the number of terms: "))
    print("Double Series:", double_series(arr))
    print("Sum of Double Series:", sum(double_series(arr)))
    print("Product of Double Series:", math.prod(double_series(arr)))
    print("Average of Double Series:", sum(double_series(arr)) / len(double_series(arr)))
    print("Length of Double Series:", len(double_series(arr)))
    print("Minimum of Double Series:", min(double_series(arr)))
    print("Maximum of Double Series:", max(double_series(arr)))
    print("Sorted Double Series:", sorted(double_series(arr)))
    print("Reversed Double Series:", reversed(double_series(arr)))

    #Output:
    # Enter the number of terms: 5
    # Double Series: [1, 2, 4, 8, 16]
    # Sum of Double Series: 31
    # Product of Double Series: 65536
    # Average of Double Series: 6.2
    # Length of Double Series: 5
    # Minimum of Double Series: 1
    # Maximum of Double Series: 16
    # Sorted Double Series: [1, 2, 4, 8, 16]
    # Reversed Double Series: [16, 8, 4, 2, 1]
