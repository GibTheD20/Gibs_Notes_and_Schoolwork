
#Part 1: Using variables, operators, expressions and function arguments to calculate the circumference.

def print_circum(radius):            #This function is designed to output the circumference when the parameter, radius, is filled with an integer. 
    print(2 * 3.14159 * radius)
    
print_circum(1)                      #The output of this function call will be 6.28318
print_circum(2)                      #The output will be 12.56636
print_circum(13)                     #The output will be 81.68133999 repeating.


print("-"*50)#This is just to separate the first part and second part of the assignment.

#Part 2: Uses variables,operators,expressions,function arguments, and concatenation to display the catalog of items.

def catalog():   #This function is made to print the catalog.
    item_1 = 200.0      #Item_1,2,3 are all static variables, they are non changing.
    item_2 = 400.0
    item_3 = 600.0  
    combo_1 = (item_1 + item_2) * .9     #Combo_1,2,3 are also variables but first they must be calculated
    combo_2 = (item_2 + item_3) * .9     #For these combo's they receive a 10% discount.
    combo_3 = (item_1 + item_3) * .9     #These variables will add 2 item variables together and multiply them by .9, or 90%.The output from these are the price after the 10% discount
    combo_4 = (item_1 + item_2 + item_3) * .75   #Combo_4 is similar to the previous combos, however this receives a 25% discount. It is multiplied by .75 because 75% of the full price is a 25% discount.

    print("Online Store")
    print("-"*22)
    print("Product(S)" + " " * 18 + "Price")
    print("Item 1" + " " * 22 + str(item_1)) #This outputs "Item 1" and 22 spaces to line up the strings under price properly. str(item_1) allows the float, 200.0 to be printed as a string.
    print("Item 2" + " " * 22 + str(item_2))
    print("Item 3" + " " * 22 + str(item_3))
    print("Combo 1(Item 1 + 2)" + " " * 9 + str(combo_1))
    print("Combo 2(Item 2 + 3)" + " " * 9 + str(combo_2))
    print("Combo 3(Item 1 + 3)" + " " * 9 + str(combo_3))
    print("Combo 4(Item 1 + 2 + 3)" + " " * 5 + str(combo_4))
    print("_" * 22)
    print("For delivery Contact:98765678899")

    
catalog()
