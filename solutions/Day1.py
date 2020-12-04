file = open("Day1Input.txt")

lines = file.readlines()

numset = {"0"}

#Part 1: find product of 2 numbers that sum to 2020
for line in lines:
    numset.add(int(line))
    if ((2020 - int(line)) in numset):
        print(line, 2020 - int(line))
        product = int(line) * (2020 - int(line))
        print("product: " + str(product))

numset.clear()

#Part 2: find product of 3 numbers that sum to 2020
for line in lines:
    numset.add(int(line))
    for num in numset:
        for num2 in numset:
            if (num + num2 + int(line) == 2020):
                print(str(num) + " " + str(num2) + " " + line)
                print("product: " + str(num*num2*int(line)))