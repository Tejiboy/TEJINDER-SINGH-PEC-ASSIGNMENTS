nums = []

for i in range(10):
    num = int(input("Enter an integer: "))
    nums.append(num)

positive_nums = []
negative_nums = []
odd_nums = []
even_nums = []
num_count = {}

for num in nums:
    if num > 0:
        positive_nums.append(num)
    elif num < 0:
        negative_nums.append(num)
    if num % 2 == 0:
        even_nums.append(num)
    else:
        odd_nums.append(num)
    if num in num_count:
        num_count[num] += 1
    else:
        num_count[num] = 1

print("Positive numbers: ", positive_nums)
print("Negative numbers: ", negative_nums)
print("Odd numbers: ", odd_nums)
print("Even numbers: ", even_nums)
print("Number of times each number occurs: ", num_count)
