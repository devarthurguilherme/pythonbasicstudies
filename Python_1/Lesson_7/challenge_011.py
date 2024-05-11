width = float(input('What is the width, in meters, of your wall? :'))
height = float(input('What is the height, in meters, of your wall? :'))
area = width * height
paint = 2
neededLiters = area / paint

print(f'Your wall has {area:.1f} m2, so you will need {neededLiters} liters')