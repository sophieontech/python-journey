import random
#import database

database = {
    9676403792: ['Sophie', 'K', 'sophiek@xyz.com', 'test1234', 150]
} #dictionary


def init():
    print("Welcome to bankSophie")
    haveAccount = int(
        input("Do you have an account with us: 1 (yes) 2 (no) \n"))
    if haveAccount == 1:
        login()
    elif haveAccount == 2:
        register()
    else:
        print("You have selected an invalid option")
    init()


def login():
    print("=== ===== ====== Login === ==== =====")

    isLoginSuccessful = False

    while isLoginSuccessful == False:
        accountNumberFromUser = int(input("What is your account number? \n"))
        passsword = input("What is your password \n")

        for accountNumber, userDetails in database.items():
            if(accountNumber == accountNumberFromUser):
                if(userDetails[3] == passsword):
                    isLoginSuccessful = True

            print('Invalid account or password')
    bankOperation(userDetails)


def register():
    print("==== Please Register ====")

    email = input("What is your email address? \n")
    fName = input("What is your first name? \n")
    lName = input("What is your last name? \n")
    password = input("Create a password for this account \n")

    accountNumber = generateAccountNumber()

    database[accountNumber] = [fName, lName, email,password]

    print("Your account has been created *****")
    print("== ==== ====== ====== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print("== ==== ====== ====== ===")
    return login()



def bankOperation(user):
    print("Welcome %s %s " % (user[0], user[1]))

    selectedOption = int(input(
        "What would you like to do? (1) deposit (2) withdrawal (3)logout (4)exit \n"))

    if(selectedOption == 1):
        depositOperation()
    elif(selectedOption == 2):
        withdrawalOperation()
    elif(selectedOption == 3):
        logout()
    elif(selectedOption == 4):
        exit()
    else:
        print("Invalid Option selected")
    bankOperation(userDetails)


def withdrawalOperation():
    print("Withdrawal")
    getCurrentBalance()
    withdrawalAmount = input("How much would you like to withdraw?: \n")
    if(getCurrentBalance > withdrawalAmount):
        withdrawalAmount -= getCurrentBalance
    return getCurrentBalance(UserDetails)


def depositOperation():
    getCurrentBalance()
    depositAmount = input("How much would you like to deposit?: \n")
    depositAmount += getCurrentBalance
    return getCurrentBalance(userDetails)


def generateAccountNumber():
    return random.randrange(1111111111, 9999999999)


def setCurrentBalance(userDetails, balance):
    userDetails[4] = balance


def getCurrentBalance(userDetails):
    return(userDetails[4])
    getCurrentBalance(userDetails)


def logout():
    login()



init()
