class user:
    username = ""
    password = ""

userList = []

"""
for i in range(3):
    newUser = user()
    newUser.username = input("input username: ")
    newUser.passWord = input("input password: ")
    userList.append(newUser)
"""

newUser = user()
newUser.username = "bob"
newUser.password = "bobisawesome"
userList.append(newUser)

print(userList[0].username)
print(userList[0].password)

"""
print(userList[1].username)
print(userList[1].password)

print(userList[2].username)
print(userList[2].password)
"""

# alex,123,bob,456,catherin,789,t
