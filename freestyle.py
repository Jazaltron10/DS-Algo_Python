import math
def new_line():
    print('Line')

def three_lines():
    new_line()
    new_line()
    new_line() 
    
def nine_lines():
    three_lines() 
    three_lines() 
    three_lines() 

def clearScreen():
    print("\nCalling clearScreen()")
    new_line()
    three_lines()
    three_lines()
    nine_lines()
    nine_lines()
    
print("\nPrinting Nine lines")    
nine_lines()
clearScreen()
    
    
    
    


def print_volume(r):
    return 4/3*(math.pi*(r**3))
    

volume_four = 4
print("\n" + str(print_volume(5+4)) + "\n")
print("\n" + str(print_volume(volume_four)) + "\n")
print("\nThe volume of the sphere of radius 9 is " + str(print_volume(9)) + "\n")



# This section is for the discussion assignment 
# Question 1 & 2
def i_will_take_your_arguments(name):
    print("Hello Hero "+ str(name) + "\n")
    

my_name = "King Jasper" 
Hero_Number = 2345
i_will_take_your_arguments("john")  # calling this function with a value
i_will_take_your_arguments(my_name) # calling this function with a variable 
i_will_take_your_arguments(Hero_Number + 2) # calling this function with an expression 




# Question 3
def Local_variable_function():
    name = "Jesse"
    age = 19
    print("My name is " + name + " and i am " + str(age) +" years old \n") 

# print(20 + age)    
Local_variable_function()

Report = " A syntax error simply occurs here because the variable age is locally defined within a function and therefore is not visible and accessible in the main function "

# Traceback (most recent call last):
# File "C:\Users\Jasper Albert Nri\PycharmProjects\DS_and_Algo\freestyle.py", line 63, in <module>
# print(20 + age)
# NameError: name 'age' is not defined




# Question 4
def Example_4(parameter_unique):
    return parameter_unique + 20
    
print(Example_4(30))
# print(parameter_unique + 50)    

report =  "Here the parameter name when used outside the function is seen as an undefined variable(i.e a variable with no value or definition), this is because the parameter passed into the function is also a local variable that just gets assigned the value of any arguments passed to the function when it is being called, so it cannot be accessed outside of it's local function within which it is defined"


# Traceback (most recent call last):
# File "C:\Users\Jasper Albert Nri\PycharmProjects\DS_and_Algo\freestyle.py", line 82, in <module>
# print(parameter_unique + 50)
# NameError: name 'parameter_unique' is not defined




# Question 5
goals = 30   
def Example_5():
    goals = 90 
    print("\nThe total amount of goals scored this year by Ronaldo is " + str(goals) + "\n")
    
Example_5()    
print("This is the value of the variable outside the function "+ str(goals) )

Report = "Again this results simply emphasizes the point of local and global variables, as can be seen even though both variables in question here share the same name they are both unaffected when operations are carried on them simultaneously, you can think of the local variable(variable contained within the function i.e CR7's goals) as a fish on a boat and the global variable(i.e variable existing outside any function) as fish in the sea, now both variables are fish of the same kind, from the sea but they each exist in very different environments, one is in a container(local variable) and the other is in the sea(global variable) on which the container sits on"


































