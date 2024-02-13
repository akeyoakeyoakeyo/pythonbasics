print("Body Mass Index (BMI) Calculator")
quiz = str(input("Do you want to know your BMI?"))
if quiz == "yes" or quiz == "Yes":

    weight = float(input("Enter your weight in kilogrammes:"))
    height = int(input("Enter your height in centimetres:"))
    height2 = height/100
    height2sq = height2*height2

    bmi = weight/height2sq
    x = round(bmi, 4)

    print(f"Your BMI is {x} kg/m2")

else:
    print("Okay! You may leave our site.")