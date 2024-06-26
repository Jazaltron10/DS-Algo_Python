# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Draw the pattern
i = 1
while i <= size:
    for j in range(size):
        print("*", end="")
    print()
    i += 1
    
    
