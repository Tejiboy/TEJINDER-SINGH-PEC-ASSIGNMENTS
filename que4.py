import math

# The number of pieces left over when the candy is divided among 5 people
remainder_5 = 2
# The number of pieces left over when the candy is divided among 6 people
remainder_6 = 3
# The number of pieces left over when the candy is divided among 7 people
remainder_7 = 2

# The maximum number of pieces in the bowl
max_pieces = 199

for pieces in range(max_pieces, 0, -1):
    if pieces % 5 == remainder_5 and pieces % 6 == remainder_6 and pieces % 7 == remainder_7:
        print("The number of pieces in the bowl is:", pieces)
        break
