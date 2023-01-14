print()
name = input("Enter you name: ")
print()

weight = int(input("Enter your weight in kg: "))

height = int(input("Enter your height in cm: "))
print()

BMI = int(weight) / ((height * height)/10000)
BMI = int(BMI)

print(f"Your BMI index is: {BMI}")
print()

if BMI>0:
    if(BMI<18.5):
        print(name +", you are underwight.")
    elif (BMI<=24.9):
        print(name +", you are normal weight.")
    elif (BMI<29.9):
        print(name +", you are overweight. You need to exercise more.")
    elif (BMI<34.9):
        print(name +", you are obese.")
    elif (BMI<39.9):
        print(name +", you are severely obese.")
    else:
        print(name +", you are morbidly obese.")
else:
    print("Enter valid input")

