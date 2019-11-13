#define square() fuction
def square(rows):
    row = "#"*rows
    for i in range(rows):
        print(row)

row_input = int(input("Enter the number of rows: "))

#call square() fuction
square(row_input)

