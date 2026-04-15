    #taking total amount as input from user
amount = int(input("Enter the total amount: "))

#calculating the number of notes of different denominations
note1 = amount // 100
note2 = (amount % 100) // 50
note3 = ((amount % 100) % 50) // 10

print("notes of 100 naira is", note1)
print("notes of 50 naira is", note2)
print("notes of 10 naira is", note3)