import string

def change_password():
    pass_checker = True
    while pass_checker:
        new_password = input("Input your new password: ")
        double = input("Input your new password again: ")
        length_valid = False
        case_valid = False
        upper_lower_valid = False
        if double == new_password:
            # go ahead with the checks
            length_valid = length_check(new_password)
            case_valid = case_check(new_password)
            upper_lower_valid = upper_lower_check(new_password)

            if length_valid == False:
                print("Please enter a password longer than 8 characters long")
            elif case_valid == False:
                print("Please use a combination of letters and numbers")
            elif upper_lower_valid == False:
                print("Please include both upper case and lower case letters")
            else:
                pass_checker = False
        else:
            print("Your password did not match")
    return new_password

def length_check(new_password):
    if len(new_password) >= 8:
        return True
    else:
        return False

def case_check(new_password):
    alpha = False
    numeric = False
    for i in range(len(new_password)):
        if new_password[i].isalpha():
            alpha = True
        if new_password[i].isdigit():
            numeric = True
        if alpha == True and numeric == True:
            return True
    return False

def upper_lower_check(new_password):
    upper = False
    lower = False
    for i in range(len(new_password)):
        if new_password[i].isalpha():
            if new_password[i].isupper():
                upper = True
            else:
                lower = True
    if upper == True and lower == True:
        return True
    else:
        return False

def main():
    class user:
        username = ""
        password = ""


def login():
    f = open("user_accounts.txt", "r")
    read = f.read()
    print(read)
    print(len(read))
    newItem = ""
    accountsList = []
    for i in range (len(read)):
        if read[i] != ",":
            newItem += read[i]
            """if i == len(read)-1:
                new = newItem
                accountsList.append(newItem)"""
        else:
            accountsList.append(newItem)
            newItem = ""
    # print(accountsList)
    for i in range (3):
        for i in range(0,len(accountsList),2):
            username = input("username: ")
            if username == accountsList[i]:
                password = input("password: ")
                userID = i
                if password == accountsList[i+1]:
                    login_details = True

            if login_details == True:
                print("pass")
                break
            else:
                print("your username or password is incorrect")








login()


