def multiple_of_7_and_divisible_by_11(start, end):
    for num in range(start, end + 1):
        if num % 7 == 0 and num % 11 == 0:
            print(num)

# Function call
multiple_of_7_and_divisible_by_11(1, 500)
