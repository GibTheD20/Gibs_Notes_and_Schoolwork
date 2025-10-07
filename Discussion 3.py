
x=int(input("Enter number:\n"))


def nested_condition(num): #Nested conditions are conditional statements contained with another conditional.

    if num > 80: #Checks to see if the number is over 80
        print("The temperature is " + str(num) + "!") #If it is, output will be the print function.

    else: # If the number is not over 80, else is executed.
        if num == 0: # After else is executed, this will run chained conditions.It will stop as soon as a statement is true
         print("The temperature is 0 get a coat!")
         print("This is a nested condition.")
         
        elif 79 >= num >= 50: # Checks to see if the variable is 50-79. If it is not, it will proceed to the next condition.If it is, it will run print functions.
         print("The temperature is " + str(num) + ", enjoy the day.")# Output is the 2 print variables below.
         print("This is a nested condition.")

        elif num <0:
            print("It is " + str(num) + " stay inside!")
            print("This is also a nested condition.")

        else: # if nothing else is true, print function will execute.
            print("The temperature is" + str(num) + ", get a jacket.")
            
    
nested_condition(x)

def chained_condition(num):  #Chained conditions are conditional statements all evaluated in sequence. Once one is true the rest are skipped.
    if num >= 80:
        print("The weather is nice, it is currently " + str(x) + ", consider suncreen")
        print("This is the beginning of the chained conditional.")

    elif num == 0:
        print("It is 0, wear a coat.")

    elif num >= 79 >= 50:
        print("It is " + str(x) + ", enjoy the day!")
        
    else:
        print("It is " + str(x) + ", consider a jacket.")
        print("This is the end of the chained conditional.")

chained_condition(x)

#Below is simplifying a nested conditional into a chained conditional.
score = int(input("Input Grade 0-100:\n"))

def nested_hard(score):
    if score >= 90:
        print("You got an A!")

    else:
        if score >=80:
           print("You got a B!")

        else:
            if  score >=70:
                print("You got a C.")

            else:
                if score >=60:
                    print("You got a D.")

                else:
                    print("You Failed!")

nested_hard(score)

def chained_easy(score):
    if score >= 90:
        print("You get an A!")
    elif score >= 80:
        print("You got a B.")
    elif score >= 70:
        print("You got a C.")
    elif score >= 60:
        print("You got a D.")
    else:
        print("You Failed!")

chained_easy(score)




