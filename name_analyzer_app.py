#  Name Analyzer App
print("This app analyzes your name!! ( dont give your real name online :P)")
name_ = input("please enter your full name: ")
if not name_.replace(" ", "").isalpha():
    print("your name has numbers in it, please enter a valid name")
else:
    name_ = name_.strip()
    print("full length of your name is: ",len(name_))
    name_ = name_.lower()
    print("lowercased version of your name", name_)
    name_ = name_.upper()
    print("uppercased version of your name", name_)
    print("\ncharacter count")
    for ch in name_: #ch is just a temporary name you give to each item you're looping through — and yes, we created it instantly for this loop only.(for my learning heh)
        if ch != " ":
            print(ch, name_.count(ch))

