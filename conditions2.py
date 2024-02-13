marks = int(input("Enter marks:"))

if marks>=80 and marks<=100:
    print("Grade : A              Excellent")
elif marks>=60 and marks<=79:
    print("Grade : B              Pass")
elif marks>=40 and marks<=59:
    print("Grade : C              Average")
elif marks>0 and marks<=39:
    print("Grade : D            Fail :(")
elif marks==0:
    print("Grade : X")
else:
    print("Wrong input")
