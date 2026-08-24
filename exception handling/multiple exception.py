try:
    num1, num2 = eval(input("Enter two numbers separated by a comma: "))
    result = num1 / num2

except ZeroDivisionError as ex:
    print("division by zero is error!!")

except SyntaxError:
    print("comma is missing. enter numbers seperated by comma like this 1, 2")

except:
    print("wrong input")

else:
    print("no exceptions")

finally:
    print("this will execute no matter what")
