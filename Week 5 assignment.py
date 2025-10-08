name = input("Enter Name:")
n = int(input("How many characters from left?:"))

#print("The first" , n , "character from the left are" , name[n:]) Mistake, it goes from n to end not 0 to n.
print("The first" , n , "character from the left are" , name[:n])

#vowels = "AEIOUaeiou" Mistakes as they are global variables, not defined within the function.
#count = 0 # According to W3Schools(n.d.) i have the option of calling a global variable however i just placed the variables inside the function for this assignment.

def all_vowels():
    vowels = "aeiouAEIOU" #Tells the program what vowels are.
    count = 0 # Count starts at 0 in case of a name having no vowels.
    for characters in name: # For every character in the name checks.
        if characters in vowels: # If the character in the name is a vowel.
            count += 1 # Adds 1 when each vowel is discovered, first loop finds A which is 0+1, second loop finds U which is 1+1 and so on.
    print("Number of vowels in name:",count)#If left in the loop then it will repeat adding 1 each time until it finishes the entire name. 

all_vowels()
        
print("Your name reversed is:", name[::-1]) # :: are left empty, leaving start and stop empty in slicing format selects the entire input, the step value being -1 tells python to move backward.


        
