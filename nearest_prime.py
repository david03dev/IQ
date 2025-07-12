def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def nearest_prime(n):
    if is_prime(n):
        return n

    offset = 1
    while True:
        lower = n - offset
        upper = n + offset
        if lower > 1 and is_prime(lower):
            return lower
        if is_prime(upper):
            return upper
        offset += 1

# Example usage:
num = int(input("Enter a number: "))
print("Nearest prime:", nearest_prime(num))
