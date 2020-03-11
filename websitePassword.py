 
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
    """Accepts a list of passwords and returns a sorted list of passwords where those passwords containing digits are accepted and the rest are rejected."""
    AcceptedList = []
    RejectedList = []
    containsDigit = False
    for password in passwordList:
        passwordContainsDigit = False
        for individualCharacter in password:
            if individualCharacter.isdigit():
                passwordContainsDigit = True     
        if passwordContainsDigit: # vs. if containsDigit == True:      containsDigit (True / False)
            AcceptedList.append(password)
        else: # elif containsDigit == False
            RejectedList.append(password)
    AcceptedRejectedList = [RejectedList, AcceptedList]
    return AcceptedRejectedList
def passLength(passwordList):
    x = containsDigit(passwordList)
    AcceptedList = x[1]
    RejectedList = x[0]
    for position, password in enumerate(AcceptedList):
        if len(password) <= 5 or len(password) >= 13:
            AcceptedList.pop(position)
            AcceptedList.insert(position, None)
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
        SymbolInPass = False
        if password.find("#") + password.find("$") + password.find("@") != -3:
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
        
        containsUpperLetter = False
        for individualCharacter in password:
            if individualCharacter.isupper() == True:
                containsUpperLetter = True
                
        if containsUpperLetter != True:
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
        
        containsLowerLetter = False
        for individualCharacters in password:
            if individualCharacters.islower() == True:
                containsLowerLetter = True
                
        if containsLowerLetter != True:
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
1. Look for logical redundancy, meaning a piece of code that is not needed. If you remove this piece of code, it should not change the behavior
or logical meaning of your code.
2. See how you can change variable names so that someone new to your code can quickly get an understanding of what your code is doing, without
having to step through every line themselves. This can be very time consuming.
3. Add a doc-string for each function explaining what the arguments are and what the output is. 

websitePassword(["TestCase23$", "Jaiden", "@fhhgh5476", "$hjghjoufd", "@#f1", "Jaiden1", "TestCase87#", "Brian93", "Jaiden2019", "Jaiden#1234", "Ud3$123456789101112", "Rq1$"])
"""
