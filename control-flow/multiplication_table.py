# multiplication_table.py

# Ask user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Use a for loop to generate the table
for i in range(1, 11):  # Loop from 1 to 10
    product = number * i
    print(f"{number} * {i} = {product}")