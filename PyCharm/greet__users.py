def greet_users(names):
    for name in names:
        msg="Hello, "+name.title()+"!"
        print(msg)
usernames=['hannah','try','margot']
greet_users(usernames)