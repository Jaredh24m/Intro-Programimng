# Areas of Shapes

# Area of a Square
side = float(input("What is the lenght of a side of the square? "))
area = side ** 2
print(f"The area of the square is: {area} ")

# Area of Rectangule
lenght = float(input("What is the Lenght of the rectangule? "))
width = float(input("What is the width of the rectangule? "))
area = lenght * width
print(f"The area of th rectangule is: {area} ")

# Area of a Circle
radius = float(input("What is the radio of the circle? "))
area = 3.14 * (radius ** 2)
print(f"The area of the circle is: {area}")

# Using math library
radius = float(input("What is the radio of the circle? "))
area = math. pi * (radius ** 2)
print(f"The area of the circle is: {area}")

# Strech 2: Many are4as from one value
value = float(input("What is the value to be used? "))
# Calculate areas
area_square = value ** 2
area_circle = math. pi *(value * 2)
volume_cube = value ** 3
volume_sphere = (4 / 3) * math. pi * (value ** 3)
# Results
print(f"Area of square is: {area_square} ")
print(f"Area of a circle is: {area_circle} ")
print(f"Area of the cube is: {volume_cube} ")
print(f"area of the sphere is: {volume_sphere}")

# Strech 3: cm > m conversion
# Area of Square
side = float(input("What is the length of a side of the square (in cm)? "))
area = side ** 2
print(f"The area of the square is: {area} cm^2")
print(f"the area of the square is: {area / 10000} m^2")

# Area of the rectangule
lenght = float(input("What is the Lenght of the rectangule? "))
width = float(input("What is the width of the rectangule? "))
area = lenght * width
print(f"The area of th rectangule is: {area} cm^2")
print(f"The area of th rectangule is: {area / 10000} m^2")

# Area of the circle
radius = float(input("What is the radio of the circle? "))
area = 3.14 * (radius ** 2)
print(f"The area of the circle is: {area} cm^2")
print(f"The area of the circle is: {area / 10000} m^2")