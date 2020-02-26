 
"""
Progress update should include a question you have as well as what you worked on since the last update.Thursday/Saturday/Monday
Mondays, thursdays
1. At least 1 letter between [a-z]
Done: 2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
Done: 3. At least 1 character from [$#@]
Done: 4. Minimum length of password: 6
Done: 5. Maximum length of password: 12
"""
def containsDigit(passwordList):
    AcceptedList = []
    RejectedList = []
    TrueFalseVar = False
    for password in passwordList:
        TrueFalseVar = False
        for individualCharacter in password:
             characterIsDigit = individualCharacter.isdigit()
             if characterIsDigit == True:
                 TrueFalseVar = True
        if TrueFalseVar == True:
            AcceptedList.append(password)
        elif TrueFalseVar == False:
            RejectedList.append(password)
    AcceptedRejectedList = [RejectedList, AcceptedList]
    return AcceptedRejectedList
def passLength(passwordList):
    x = containsDigit(passwordList)
    AcceptedList = x[1]
    RejectedList = x[0]
    for password in AcceptedList:
        passPos = 0
        if len(password) <= 5 or len(password) >= 13:
            for position, value in enumerate(AcceptedList):
                if value == password:
                    passPos = position
                    AcceptedList.pop(passPos)
                    AcceptedList.insert(passPos, None)
                    RejectedList.append(password)
    AcceptedRejectedList = [RejectedList, AcceptedList]
    return AcceptedRejectedList
def containsSpecialCharacters(passwordList): #creates the new function(problem area)
    x = passLength(passwordList)
    AcceptedList = x[1]
    RejectedList = x[0]
    for password in AcceptedList:
        if password == None:
            continue
        if password.find("#") + password.find("$") + password.find("@") == -3:
            SymbolInPass = False
        else:
            SymbolInPass = True
        if SymbolInPass == False:
            x = AcceptedList.index(password)
            AcceptedList.pop(x)
            AcceptedList.insert(x, None)
            RejectedList.append(password)
    AcceptedRejectedList = [RejectedList, AcceptedList]
    return AcceptedRejectedList

def containsUpper(passwordList):
    x = containsSpecialCharacters(passwordList)
    AcceptedList = x[1]
    RejectedList = x[0]
    for password in AcceptedList:
        if password == None:
            continue
        TrueFalseVar = False
        for individualCharacters in password:
            if individualCharacters.isupper() == True:
                TrueFalseVar = True
        if TrueFalseVar != True:
            x = AcceptedList.index(password)
            AcceptedList.pop(x)
            AcceptedList.insert(x, None)
            RejectedList.append(password)
    
    AcceptedRejectedList = [RejectedList, AcceptedList]
    return AcceptedRejectedList
            
def containsLower(passwordList):
    x = containsUpper(passwordList)
    AcceptedList = x[1]
    RejectedList = x[0]
    for password in AcceptedList:
        if password == None:
            continue
        TrueFalseVar = False
        for individualCharacters in password:
            if individualCharacters.islower() == True:
                TrueFalseVar = True
        if TrueFalseVar != True:
            x = AcceptedList.index(password)
            AcceptedList.pop(x)
            AcceptedList.insert(x, None)
            RejectedList.append(password)
    AcceptedRejectedList = [RejectedList, AcceptedList]
    return AcceptedRejectedList

def websitePassword(passwordList):
    x = containsLower(passwordList)
    AcceptedList = x[1]
    RejectedList = x[0]
    while (None in AcceptedList):
        AcceptedList.remove(None)
        #while (AcceptedList.find(None) != -1

    dictionary = {"Accepted Passwords": AcceptedList,"Rejected Passwords": RejectedList} #go back to this
    print(dictionary)

    
"""
websitePassword(["TestCase23$", "Jaiden", "@fhhgh5476", "$hjghjoufd", "@#f1", "Jaiden1", "TestCase87#", "Brian93", "Jaiden2019", "Jaiden#1234"])
"""
