import math

lengths = [50, 60, 70, 80, 90]

for length in lengths:
    t_square = (4 * ((math.pi) ** 2) * length) / (9.8 * 100)
    print(t_square)