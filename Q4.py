# Input the three angles of a triangle

angle1 = int(input("enter the first angle: "))
angle2 = int(input("enter the second angle: "))
angle3 = int(input("enter the third angle: "))

if angle1 + angle2 + angle3 == 180:
    print("triangle is valid")

else :
    print("triangle is not valid")