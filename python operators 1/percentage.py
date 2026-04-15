#take marks as input from the user
print ("enter marks obtained in 4 subjects: ")
maths = int(input("maths: "))
physics = int(input("physics: "))
chemistry = int(input("chemistry: "))
biology = int(input("biology: "))

#lets calculate the percentage of marks
sum = maths + physics + chemistry + biology
print ("sum of maths, physics, chemistry and biology is", sum)
percentage = (sum / 400) * 100
print (end = "percentage of marks is: ")
print (percentage, "%")