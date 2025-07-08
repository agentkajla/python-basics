# simple calculator with match case statement
print("Hey welcome to my simple calculator")

num_1 = float(input("enter your first digit: "))
opp_ = (input(" enter your operation: "))
num_2 = float(input("enter your second digit: "))

match opp_:
    case "+":
        print(num_1 + num_2)
    case "-":
        print(num_1-num_2)
    case "*":
        print(num_1*num_2)
    case "/":
        if num_2 != 0:
            print(num_1/num_2)
        else:
            print("cant divide by 0")
    case _:
        print("invalid!! :/")
            

