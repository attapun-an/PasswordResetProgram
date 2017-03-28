
# for appending to the array
def array_create():
    f = open("user_accounts.txt", "r")
    read = f.read()
    # doesn't work too well due to the comma I placed at the end
    accountsList = read.split(',')
    print(accountsList)


def array_create_2():
    f = open("user_accounts.txt", "r")
    read = f.read()
    # print(read)
    # print(len(read))
    newItem = ""
    accountsList = []
    for i in range (len(read)):
        if read[i] != ",":
            newItem += read[i]
            if i == len(read)-1:
                new = newItem.strip('/n')
                accountsList.append(newItem.strip("/n"))
        else:
            accountsList.append(newItem)
            newItem = ""
            f.close()
    return accountsList

numList = array_create_2()
print(numList)
