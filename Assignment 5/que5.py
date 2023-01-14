n = int(input("Enter the number of rows: "))
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_index = 0

for i in range(1,n+1):
    for j in range(i):
        print(alphabet[alphabet_index], end = "")
        alphabet_index += 1
        if alphabet_index == 26:
            alphabet_index = 0
    print("")
