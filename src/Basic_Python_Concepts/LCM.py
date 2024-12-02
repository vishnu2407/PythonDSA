import math

def lcm(a, b):
    return a * b // math.gcd(a, b)


if __name__ == "__main__":
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("The LCM of", a, "and", b, "is", lcm(a, b))
    print("The GCD of", a, "and", b, "is", math.gcd(a, b))