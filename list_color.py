import random
colors = []  # list colors
for x in range(23):
    colors.append('black')

for x in range(16):
    colors.append('red')

for x in range(8):
    colors.append('blue')

for x in range(2):
    colors.append('green')

for x in range(1):
    colors.append('yellow')

random.shuffle(colors)
print(colors)
