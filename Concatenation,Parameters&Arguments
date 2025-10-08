def date(d, m, y): #Three parameters: d m y.
    result = str(d) + '/' + str(m) + '/' + str(y) #Example of concatenation, combining strings with
    return result

print(date(14, 9, 2025)) # Three arguments: 14,9,2025, arguments are what fill paramaters.

day = 14 # S
def print_three():
    print(date(14,9,2025)) #Argument using a value.
    print(date(day,9,2025)) #Arguments using a variable.
    print(date(13+1,9,2025)) #Argument using an expression

print_three() #All outputs are the same, using either variable(day),expressions(13+1), and a value(14).

def name():
    insidename = 'Austin' #Local name is inside the function.
    print(insidename)
    return insidename

name()
print(insidename) #Since insidename is defined inside the function,if you try to call it you will receive a name error. This shows that local variables cannot be accessed outside of the function. REMOVE this for code to work.


def name_date(person_name, d,m,y): # person_name is the parameter
    date_str = str(d) + '/' + str(m) + '/' + str(y)
    message = "Your name is " + person_name + ", and the date is " + date_str
    print(message)
    return message

name_date("Austin", 14 , 9 , 2025)
print(person_name) #Attempting to call a parameter that is defined inside function returns error as person_name only exists inside the function.REMOVE this for code to work

name = "OutsideName" #Out of function name
def variable_test():
    name = "InsideName" #Inside function name
    print("Inside Function:", name) #Prints inside function, then the name variable defined inside the function.

variable_test()
print("Outside function", name) #Shows that global variables, name = "Outside name" , which are variables made outside of a function do not interfere with variables made inside the function.

