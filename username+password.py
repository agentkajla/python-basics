# Simple login system (username + password)
print("Hello sir please log yourself in to use our program")
user = input("please tell us your username and remember it please: ")
password = int(input("now please enter your password and remember it too: "))

print("now please sign up in your account you just created!")
check_user = input("user: ")
check_pass = int(input("password: "))

if ( user == check_user and password == check_pass):
    print("your login info was correct you can enter in site now")
else:
    print("please enter a valid info!! :/")
