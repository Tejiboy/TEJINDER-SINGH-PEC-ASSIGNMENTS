import random

score = 0

for i in range(1,11):
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    answer = num1 * num2
    player_answer = int(input(f"Question {i}: {num1} x {num2} = "))
    if player_answer == answer:
        print("Right!")
        score += 1
    else:
        print(f"Wrong. The answer is {answer}.")

print(f"You got {score} out of 10 questions right.")
