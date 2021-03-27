from datetime import datetime
now = datetime.now()

name = input("What is your name? \n")
allowedUsers = ['Sophie', 'Marie', 'Amaa', 'Test']
allowedPassword = ['PasswordSophie', 'PasswordMarie', 'PasswordTest']
allowedAmount = [10,20,50,100]

if(name in allowedUsers):
    password = input('Your password? \n')
    userId = allowedUsers.index(name)   

    if (password == allowedPassword[userId]):
        print('Welcome %s' %name + ' ' + str(now))      
        print('These are the available Options:')
        print('1, Withdrawal')
        print('2, Cash Deposit')
        print('3, Complaint')
        selectedOption = int(input('Please select an option:'))
        print(selectedOption)
        if(selectedOption == 1):
            toWithdraw=input('How much would you like to withdraw?')
            print('take your cash')
        elif(selectedOption == 2):
            toDeposit=input('How much would you like to deposit?')
            print(str('Your Balance is' + ' '+ toDeposit))
        elif(selectedOption == 3):
            complaintmsg = input('What is your complaint? \n')
            print(complaintmsg)
            print("Thank you for contacting us!")
        else:
            print('Invalid Option chosen, please try again')
    else:
        print('Password Incorrect, Please try again')
else:
    print('Name not found. Try again')
                                                       