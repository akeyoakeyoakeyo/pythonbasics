name = str(input("Enter a name:"))

# if name.lower() == name.upper():
#     print(f"{name} is a palindrome")
# else:
#     print(f"{name} is not a palindrome")

for y in name:
    if y == name[0]:
        print(name, "is a palindrome")