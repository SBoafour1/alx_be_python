# pattern_drawing.py

# Prompt User for Pattern Size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop for rows
while row < size:
    # Use for loop for columns
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
