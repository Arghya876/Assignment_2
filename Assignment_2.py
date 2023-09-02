# Find the Area of a Square

def area(side_length):
    square_area = side_length ** 2
    return square_area

side_length = float(input("Enter the side length of the square: "))

result = area(side_length)

print(f"The area of the square is {result}")
