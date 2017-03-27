import string
print(string.punctuation)

class user:
    username = ""
    password = ""

userList = []

newUser = user()
newUser.username = "bob"
newUser.password = "bobisawesome"
userList.append(newUser)

print(userList[0].username)
print(userList[0].password)

f = open("user_accounts.txt", "w")
f.write(newUser.username + "," + newUser.password)


