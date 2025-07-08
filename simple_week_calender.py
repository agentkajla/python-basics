# simple app that tells you about what day it is on the date
print("Hello this is a week day calender \nexample:\n1. monday \n2.tuesday \n3.wednesday \n4.thrusday \n5.friday \n6.saturday \n7.sunday")

num_0 = int(input("enter the day you wanna know: "))

match num_0:
    case 1:
        print("Hey you choose monday")
    case 2:
        print("Hey you choose tuseday ")
    case 3:
        print("Hey you choose wednesday")
    case 4:
        print("Hey you choose thrusday")
    case 5:
        print("Hey you choose friday")
    case 6:
        print("Hey you choose saturaday")
    case 7:
        print("Hey you choose sunday ")
    case _:
        print("LMFAO there's no day on that number ")