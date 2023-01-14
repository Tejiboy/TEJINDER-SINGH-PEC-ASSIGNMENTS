def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)

# Input from user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Function call
print_primes(start, end)
