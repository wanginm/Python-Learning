import json
filename='username.json'
try:
    with open(filename)as f_obj:
        username=json.load(f_obj)
except FileNotFoundError:
    username=input("What is your name? ")
    with open(filename)as f_obj:
        json.dump(username,f_obj)
        print("We will remember you when you come back, "+username+"!")
else:
    print("Weclome back, "+username+"!")