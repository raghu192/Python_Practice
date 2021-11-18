# take triangle side lentghs from the user
ab=int(input())
bc=int(input())
ca=int(input())
if ab==bc==ca:
    print("the triangle is equilateral")
elif (ab==bc) or (bc==ca) or (ca==ab):
    print("the triangle is isosceles")
else:
    print("the triangle is scalene")

