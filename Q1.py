
# Function to check if it's a right-angled triangle



def is_right_angled(a, b, c):
    sides = sorted([a, b, c]) 

    # Sort the sides to apply Pythagoras theorem
    
    return sides[0]**2 + sides[1]**2 == sides[2]**2



def classify_triangle(a, b, c):
    if a == b == c:
        return "Equilateral Triangle"
    elif a == b or b == c or a == c:
        if is_right_angled(a, b, c):
            return "Isosceles and Right-Angled Triangle"
        return "Isosceles Triangle"
    elif is_right_angled(a, b, c):
        return "Scalene and Right-Angled Triangle"
    else:
        return "Scalene Triangle"




a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))



if a + b > c and b + c > a and c + a > b:
    triangle_type = classify_triangle(a, b, c)
    print(f"The triangle is a {triangle_type}.")
else:
    print("The given sides do not form a valid triangle.")
