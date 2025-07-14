# String Slicer Tool
print("this tool helps you to slice strings as the name says")

str_ = str(input("enter the string you want to slice: "))
inp_ = input("enter the input you want:\n1.Show first 3 letters? \n2.From index 2 to 5? \n3.Reverse the string? \n4.Every 2nd letter only?" )
match inp_:
    case "1":
        print("here are first three letters of your string: ", str_[0:3])
    case "2":
        print("here's your string from index 2 to 5: ", str_[2:6])
    case "3":
        print("here's your string in reverse: ", str_[::-1])
    case "4":
        print("here's your string's every 2 letter: ", str_[::2] )
    case _:
        print("invalid input")