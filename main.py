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

def import_accounts_list():
    f = open("user_accounts.txt", "r")
    read = f.read()
    # print(read)
    # print(len(read))
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
            f.close()
    return accountsList

def modify_accounts_list(userID, new_password):
    accountsList= import_accounts_list()
    accountsList[int(userID)+1] = new_password
    write_accounts_list(accountsList)

def write_accounts_list(accountsList):
    f = open("user_accounts.txt", "w")
    for i in range(len(accountsList)):
        f.write(accountsList[i] + ",")
    f.close()


def login():
    accountsList = import_accounts_list()
    # print(accountsList)
    for i in range (3):
        un = False
        pw = False
        username = input("username: ")
        password = input("password: ")
        for i in range(0,len(accountsList),2):
            if username == accountsList[i]:
                userID = i
                un = True
            if password == accountsList[i+1]:
                pw = True

        if un == True and pw == True:
            return userID
        else:
            print("your username or password is incorrect")
            if i == 3:
                return ""

def self_destruct_sequence():
    import webbrowser
    f = open("spam.txt", "w")
    new = 2 # open in a new tab, if possible

    # open a public URL, in this case, the webbrowser docs
    url = "https://www.youtube.com/watch?v=8ZcmTl_1ER8"
    webbrowser.open(url, new=new)
    while True:
        f.write("KAPOW")
        new = 2 # open in a new tab, if possible

        # open a public URL, in this case, the webbrowser docs
        url = "https://www.google.co.th/?gws_rd=cr&ei=szvZWPyTKcTevgSCjIjgBA"
        webbrowser.open(url, new=new)

# def strength_test():

def main():
    import sys
    userID = login()
    # will exit the program or self destruct if null user ID is returned
    if userID == "":
        reaction = input("""you have failed, would you like to:
        1) stop the script from running
        2) initiate self destruct sequence""")
        if reaction == "2":
            print("the computer will now self destruct")
            self_destruct_sequence()
        else:
            sys.exit()
    new_password = change_password()
    modify_accounts_list(userID, new_password)
    print("your password has been saved")

main()


