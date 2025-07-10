# Odd/Even & Multiplication Table Combo Tool
print("welcome to my tool that checks your given number if it's odd or even and gives you a multiplication table of it")
num_ = int(input("please enter your number: "))
if(num_ % 2 == 0):
    print("your number is even!!")
    
else:
    print("your number is odd")
print("Here is the multiplication table of number: ", num_)
for i in range(1, 11):
        print(num_, "*" , i, "=", (num_*i))
    