def fibonacci(n):
    """Return the nth Fibonacci number using recursion."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def gcd(a, b):
    """Return the greatest common divisor of a and b using Euclid's algorithm (recursively)."""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def compareTo(s1, s2):
    """
    Recursively compare two strings.
    Return a negative number if s1 < s2,
    0 if s1 == s2,
    a positive number if s1 > s2.
    """
    if s1 == "" and s2 == "":
        return 0
    if s1 == "":
        return -ord(s2[0])
    if s2 == "":
        return ord(s1[0])
    if s1[0] != s2[0]:
        return ord(s1[0]) - ord(s2[0])
    return compareTo(s1[1:], s2[1:])


# Test cases
if __name__ == "__main__":
    print("Fibonacci(6):", fibonacci(6))               # Expected: 8
    print("GCD(48, 18):", gcd(48, 18))                 # Expected: 6
    print('compareTo("apple", "apples"):', compareTo("apple", "apples"))   # Expected: negative
    print('compareTo("zebra", "apple"):', compareTo("zebra", "apple"))     # Expected: positive
    print('compareTo("cat", "cat"):', compareTo("cat", "cat"))             # Expected: 0
