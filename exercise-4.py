# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

print("Enter the lengths of three side of a triangle: ")
sideA = int(input("a: "))
sideB = int(input("b: "))
sideC = int(input("c: "))

if sideA == sideB == sideC:
	print("A triangle with sides of " + str(sideA) + " " + str(sideB) + " " + str(sideC) + " is a " + "Equilateral triangle")
elif sideA==sideB or sideB==sideC or sideC==sideA:
	print("A triangle with sides of " + str(sideA) + " " + str(sideB) + " " + str(sideC) + " is a " + "isosceles triangle")
else:
	print("A triangle with sides of " + str(sideA) + " " + str(sideB) + " " + str(sideC) + " is a " + "Scalene triangle")