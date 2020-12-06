file = open("solutions/Day6Input.txt")

text = file.read()

split_text = text.split("\n\n")

#part1
clean_text = []
sum = 0

for entry in split_text:
    #remove \ns
    clean_text.append(entry.replace('\n', ' '))

for entry in clean_text:
    s = set(entry)
    l = len(s)
    sum+=l

print("number of answers selected yes: " + str(sum))

#part2
sets = []
allsum = 0

for entry in clean_text:
    answers = entry.split(" ")
    for people in answers:
        sets.append(set(people))
    allsum += len(set.intersection(*sets))
    sets.clear()
    
print("number of answers everyone selected yes: " + str(allsum))