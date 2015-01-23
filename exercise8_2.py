def replace_char(x, y, old_color, new_color):
    

l = []

with open("textmap.txt", 'r') as f:
    for line in f:
        l.append([])
        for character in line:
             if character != '\n':
                l[-1].append(character)

l[8][9] = "A"

for row in l:
    print(row)