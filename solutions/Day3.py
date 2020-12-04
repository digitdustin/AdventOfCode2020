file = open("Day3Input.txt")

lines = file.readlines()[1:]

slope_width = 31
increments = [1, 3, 5, 7, 1]
position = [1, 3, 5, 7, 1]
# Right1, down 1
# Right3, down 1
# Right5, down 1
# Right7, down 1
# Right1, down 2
tree_counter = [0, 0, 0, 0, 0]
last_path = False

for line in lines:
    for i in range(len(position)):
        if i != 4:
            if position[i] < slope_width:
                if line[position[i]] == '#':
                    tree_counter[i] += 1
            else:
                if line[position[i] % slope_width] == '#':
                    tree_counter[i] += 1
            position[i] += increments[i]
        else:
            if last_path:
                if position[i] < slope_width:
                    if line[position[i]] == '#':
                        tree_counter[i] += 1
                else:
                    if line[position[i] % slope_width] == '#':
                        tree_counter[i] += 1
                position[i] += increments[i]
            last_path = not last_path

print(tree_counter)

product = 1

for vals in tree_counter:
    product *= vals
    
print(product)