# Pattern 1: Square
size = 5
for i in range(size):
    print('* ' * size)

# Pattern 2: Right Triangle (Right-aligned)
size = 5
for i in range(1, size + 1):
    print(' ' * (size - i) + '* ' * i)

# Pattern 3: Equilateral Triangle
size = 5
for i in range(1, size + 1):
    print(' ' * (size - i) + '* ' * (2 * i - 1))

# Pattern 4: Hollow Square
size = 5
print('* ' * size)
for i in range(size - 2):
    print('* ' + '  ' * (size - 2) + '* ')
if size > 1:
    print('* ' * size)

# Pattern 5: Pyramid
size = 5
for i in range(1, size + 1):
    print(' ' * (size - i) + '* ' * (2 * i - 1))

# Pattern 6: Inverted Pyramid
size = 5
for i in range(size, 0, -1):
    print(' ' * (size - i) + '* ' * (2 * i - 1))

# Pattern 7: Diamond
size = 5
for i in range(1, size + 1):
    print(' ' * (size - i) + '* ' * (2 * i - 1))
for i in range(size - 1, 0, -1):
    print(' ' * (size - i) + '* ' * (2 * i - 1))

# Pattern 8: Left-aligned Triangle
size = 5
for i in range(1, size + 1):
    print('* ' * i)

# Pattern 9: Number Triangle
size = 5
for i in range(1, size + 1):
    print(str(i) * i)

# Pattern 10: Hourglass Pattern
size = 5
for i in range(size, 0, -1):
    print(' ' * (size - i) + '* ' * (2 * i - 1))
for i in range(2, size + 1):
    print(' ' * (size - i) + '* ' * (2 * i - 1))

# Pattern 11: Hollow Right Triangle
size = 5
for i in range(1, size + 1):
    if i == 1 or i == size:
        print('* ' * i)
    else:
        print('* ' + '  ' * (i - 2) + '* ')

# Pattern 12: Hollow Pyramid
size = 5
for i in range(1, size + 1):
    if i == size:
        print('* ' * (2 * i - 1))
    else:
        print(' ' * (size - i) + '* ' + '  ' * (2 * i - 3) + '* ' * (i > 1))

# Pattern 13: Floyd's Triangle
size = 5
num = 1
for i in range(1, size + 1):
    for j in range(i):
        print(num, end=' ')
        num += 1
    print()


# Pattern 14: Pascal's Triangle
size = 5
for i in range(size):
    print(' ' * (size - i), end='')
    num = 1
    for j in range(i + 1):
        print(num, end=' ')
        num = num * (i - j) // (j + 1)
    print()

# Pattern 15: Butterfly Pattern
size = 5
for i in range(1, size + 1):
    print('* ' * i + '  ' * (size - i) + '* ' * i)
for i in range(size, 0, -1):
    print('* ' * i + '  ' * (size - i) + '* ' * i)
