file = open("Day4Input.txt") 

file_data = file.read()

lines = file_data.split("\n\n")

eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
hair_colors = ["a", "b", "c", "d", "e", "f", "1", "2", "3", "4" ,"5" , "6" , "7" , "8" , "9", "0"]

def check(data):
    for val in data:
        if (val[0] == "byr"):
            if (int(val[1]) < 1920 or int(val[1]) > 2002):
                return False
        elif (val[0] == "iyr"):
            if (int(val[1]) < 2010 or int(val[1]) > 2020):
                return False
        elif (val[0] == "eyr"):
            if (int(val[1]) < 2020 or int(val[1]) > 2030):
                return False
        elif (val[0] == "hgt"):
            if (val[1][-2:] == "cm"):
                if (int(val[1][:-2]) < 150 or int(val[1][:-2]) > 193):
                    return False
            elif (val[1][-2:] == "in"):
                if (int(val[1][:-2]) < 59 or int(val[1][:-2]) > 76):
                    return False
            else: 
                return False
        elif (val[0] == "hcl"):
            if (val[1][0] != "#" or len(val[1][1:]) != 6):
                return False
            for char in val[1][1:]:
                if char not in hair_colors:
                    return False
        elif (val[0] == "ecl"):
            if (val[1] not in eye_colors):
                return False
        elif (val[0] == "pid"):
            if (len(val[1]) != 9 or not val[1].isnumeric()):
                return False
        elif (val[0] == "cid"):
            #do nothing
            if (not val[1].isnumeric):
                return False
            
    return True

count = 0

newMap = []

for line in lines:
    s = line.replace("\n", " ")
    z = s.split(" ")

    mapAdd = []
    if ("byr" in line and "iyr" in line and "eyr" in line and "hgt" in line and "hcl" in line and "ecl" in line and "pid" in line):
        for l in z:
            mapAdd.append(l.split(":"))
        newMap.append(mapAdd)

print((len(newMap)))

for entry in newMap:
    if (check(entry)):
        count += 1


print(count)
    