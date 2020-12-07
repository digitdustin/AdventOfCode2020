file = open("solutions/Day7Input.txt")

rules = file.readlines()

count = 0

colors = ["shiny gold"]
colors_set = {"shiny gold"}

def findBags(rules, color):
    for rule in rules:
        if color in rule[5:]:
            s = rule.split()
            container = s[0] + " " + s[1]
            colors_set.add(container)
            findBags(rules, container)

findBags(rules, "shiny gold")

print(colors_set)
print(len(colors_set))

#part2



def findNumBags(rules, color):

    for rule in rules:
        s = rule.split()
        bag = s[0] + " " + s[1]
        if bag == color:
            if s[5] == "no":
                #bag contains no bags, do nothing
                return 0
            else:
                numBags = int((len(s) / 4) - 1)
                for i in range(numBags):
                    return int(s[(i*4)+4]) * findNumBags(rules, s[(i*4) + 5] + " " + s[(i*4) + 6])
        return 
                    

print("done")
num = 0
s = findNumBags(rules,"shiny gold")
print(s)
