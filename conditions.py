num = int(input("Enter number:"))

if num % 2 == 0:
    print(f"Variable {num} is an even number")
else:
    print(f"Variable {num} is an odd number")

age = int(input("Enter age:"))

if age < 18:
    print(f"You can't vote as at now. You will be eligible to vote in {18-age} years")
elif age > 100 :
    print("Kindly enter a valid age.")
else:
    print("Congratulations! You are eligible to vote.")


