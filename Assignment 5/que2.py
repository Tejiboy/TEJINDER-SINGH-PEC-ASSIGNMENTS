# Function to print all numbers divisible by a given number in a range
def print_divisible_numbers(start, end, divisor):
    for i in range(start, end+1):
        if i % divisor == 0:
            print(i)

# Input from user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
divisor = int(input("Enter the divisor: "))

# Function call
print_divisible_numbers(start, end, divisor)
