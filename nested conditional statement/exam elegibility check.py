medical_course = input("do you take medical course? (yes/no) ")
atten = int(input("enter the attendance of the student "))
if medical_course == "yes":
    print("you are eligible for the exam")
else:
    if atten >= 75:
        print("you are eligible for the exam")
    else:
        print("you are not eligible for the exam")

