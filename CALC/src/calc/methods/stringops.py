def validationNumber(a):
    numbers  = ["1","2","3","4","5","6","7","8","9","0","."]
    if str(a) in numbers:
        return True
    else:
        return False    
    
def validationOper(b):
    numbers  = ["(",")","+","-","/","*"]
    if str(b) in numbers:
        return True
    else:
        return False    
    
def stringToarrey(intitalString):
    ecuation=[]
    number=""
    for i in range(len(intitalString)):
        number_to_check = intitalString[i]
        #print(validationNumber(number_to_check),validationOper(number_to_check))
        if validationOper(number_to_check):
            if len(number)>0: 
                ecuation.append(number)
            number=""
            ecuation.append(number_to_check)
        if validationNumber(number_to_check):
            number = number + str(number_to_check)
    if len(number)>0: 
        ecuation.append(number)
    return ecuation

def strangValidation(stringToValidate):
    validString=True 
    #valida el numero de ()
    if stringToValidate.count("(") % 2 !=0:
        validString=False 
    if stringToValidate.count(")") % 2 !=0:
        validString=False

   # validString=is_number(stringToValidate)
    return validString

def is_number(stringEntry):
    for s in range(len(stringEntry)):
        try:
            # Try to convert the string to an integer or float
            int(s)  # For integer
            return True
        except ValueError:
            try:
                float(s)  # For float
                return True
            except ValueError:
                flag=False
                #flag=validationOper(s)
                return flag