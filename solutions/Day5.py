file = open("solutions/Day5Input.txt") 

rows = file.readlines()

print(rows)

STARTING_VAL = 128

seat_ids = []

for row in rows:
    vals = [0, 127]
    colvals = [0, 7]
    for i in range(7):
        if row[i] == 'F':
            #change values to lower half
            vals[1] = int(((int(vals[1]) - int(vals[0])) / int(2))) + int(vals[0])#int(int(vals[1]) / int(2))
        elif row[i] == 'B':
            vals[0] = int((((int(vals[1]) - int(vals[0])) + 1) / int(2))) + int(vals[0])
        #vals now contains the row number
    for i in range(3):
        if row[7 + i] == 'L':
            colvals[1] = int(((int(colvals[1]) - int(colvals[0])) / int(2))) + int(colvals[0])#int(int(vals[1]) / int(2))
        elif row[7 + i] == 'R':
            colvals[0] = int((((int(colvals[1]) - int(colvals[0])) + 1) / int(2))) + int(colvals[0])
    seat_ids.append((vals[0] * 8) + colvals[0])

print(max(seat_ids))

seat_ids.sort()

print(seat_ids)

for val in seat_ids:
    if val + 1 not in seat_ids:
        print (val + 1)