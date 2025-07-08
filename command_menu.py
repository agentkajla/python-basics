# simple command menu ( start, help, quit)
print("1. Start \n2. Help \n3. Settings \n4. Quit")

cmd = int(input(" please enter your desired command: "))

match cmd:
    case 1:
        print("the application is loading please wait...")
    case 2:
        print("The help window is loading please wait...")
    case 3:
        print("The settings window is loading please wait...")
    case 4:
        print("quitting the program meet you again, sir  ")
    case _:
        print("seems like you entered something wrong gang ")