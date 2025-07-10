# login /signup system
print("welcome to our app please sign yourself in!!")
user_ = input("please enter your username= ").strip()
pass_ = input("please enter your password= ").strip()

print(" nice now you're signed in perfectly now please log yourself again so we can check if it's you!")
user_0 = input("USERNAME: ").strip()
pass_0 = input("PASSWORD: ").strip()

if ( user_0 == user_ and pass_0 == pass_):
    print("welcome", user_.capitalize(), "enjoy our website/application!")
    print("please remember your username","*" * len(user_), "and your password", "*" * len(pass_))
else:
    print("Invalid login please try a vaild one!!  ")

