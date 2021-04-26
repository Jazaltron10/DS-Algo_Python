import math

# Written Assignment
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
    
    
    
    

# Learning Journal 
#Question 1
def print_volume(r):
    return 4/3*(math.pi*(r**3))
    

volume_four = 4
print("\n" + str(print_volume(5+4)) + "\n")
print("\n" + str(print_volume(volume_four)) + "\n")
print("\nThe volume of the sphere of radius 9 is " + str(print_volume(9)) + "\n")



# Question 2
def FootballStatistics(playerName, goals , assists ):
    print("\nThe total number of goals scored by " + playerName + " this year is " + str(goals) + " goals")
    print("The total number of assists given by " + playerName + " this year is " + str(assists) + " assists\n") 
    
    
FootballStatistics("Cristiano Ronaldo", 60, 25)
FootballStatistics("Kylian Mbappe", 40, 10)
FootballStatistics("Lionel Messi", 55, 35)





# This section is for the Discussion Assignment 
# Question 1 & 2
def i_will_take_your_arguments(name):
    print("Hello Hero "+ str(name) + "\n")
    

my_name = "King Ronaldo" 
Hero_Number = 2345

# calling this function with a string value
i_will_take_your_arguments("Kawaki") 

# calling this function with a user defined variable
i_will_take_your_arguments(my_name)  

# calling this function with an expression 
i_will_take_your_arguments(Hero_Number + 2) 


"""
Explanation Q1:
Here I defined a function that takes in a parameter, which will be passed in as an argument when the function is called.
In this function the variable passed in when the function is being defined(i.e name) is what is called a parameter,
While the value being passed into the function when it is being called at the bottom is called the argument (in this case the string "john").

Explanation Q2:
After defining the function, I called it three times.
The First call was by passing a string value into the function, and that was parsedin as the argument of this function.
The Second call was by passing a variable I defined and initialized with a string value.
The Third call was done by passing in an expression, which in itself contained a variable of type integer being added to a basic integer data type.

Summary: 
I defined a function that takes in an argument and i passed three different types of arguments namely a value, a variable and an expression
I also had to use the built-in str() function this is because only strings can be passed in to the print() function.
Lastly all values passed into a function being called are called the arguments of that function and the respective value of that argument gets
assigned to the function parameter which performs logical operations with the value passed in within the said function.
"""


# Question 3
def Local_variable_function():
    name = "Jesse"
    age = 19
    print("My name is " + name + " and i am " + str(age) +" years old \n") 

print(20 + age)    
Local_variable_function()


# Results
# Traceback (most recent call last):
# File "C:\Users\Jasper Albert Nri\PycharmProjects\DS_and_Algo\freestyle.py", line 63, in <module>
# print(20 + age)
# NameError: name 'age' is not defined

"""
Explanation:
What Happens:
When i tried to use the local variable i created outside my function i defined i encountered a syntax error
Which is a break in the structure of the program that prevents it from being interpreted
A syntax error simply occurs here because the variable age is locally defined within 
the function "Local_variable_function" and therefore is not visible and accessible in the main function.
But when i comment the statement causing the error and call the function it gets parsed and interpreted 
giving the intended result.

Results:
The Traceback shows the most recent function call made within the python file.
File shows the directory of the python file where the error occurred.
The third line is the acual statement that caused the error.
The last infomation to be logged with the error is the NameError message which simply indicates that the 
Variable "age" i am trying to use is not globally defined and therefore not accessible to the main function.
"""


# Question 4
def Example_4(parameter_unique):
    return parameter_unique + 20
    
print(Example_4(30))
print(parameter_unique + 50)    


# Traceback (most recent call last):
# File "C:\Users\Jasper Albert Nri\PycharmProjects\DS_and_Algo\freestyle.py", line 82, in <module>
# print(parameter_unique + 50)
# NameError: name 'parameter_unique' is not defined

"""
Explanation:
What Happens:
Here the parameter name when used outside the function is seen as an undefined variable(i.e a variable with no value or definition), 
this is because the parameter passed into the function is also a local variable within the function. 
It just gets assigned the value of any arguments passed to the function when it is being called, 
so it cannot be accessed outside of it's local function within which it is defined

Results:
Here i get the same error message as before when i tried to use a locally defined variable outside of it's function or in a global context.
We get the Traceback which tells us the latest function to be called,
we get the file directory of the python file and the line number which the error occurred,
Then we get the statement causing the error,
and Lastly we get a NameError as this is a local variable being used globally. 
"""


# Question 5
goals = 30   
def Example_5():
    goals = 90 
    print("\nThe total amount of goals scored this year by Ronaldo is " + str(goals) + "\n")
    
Example_5()    
print("This is the value of the variable outside the function "+ str(goals) )



"""
Explanation:
What Happens:
Again this results simply emphasizes the point of local and global variables, as can be seen even though both variables in question here share the same name they are both unaffected when operations are carried on them simultaneously, you can think of the local variable(variable contained within the function i.e CR7's goals) as a fish on a boat and the global variable(i.e variable existing outside any function) as fish in the sea, now both variables are fish of the same kind, from the sea but they each exist in very different environments, one is in a container(local variable) and the other is in the sea(global variable) on which the container sits on.

Results:
We get no error here this is because the variable being used here even though it is defined locally, it is also defined globally.
"""

import math
# Question 1
print ('Hello world \n')

def print_volume(r):
    volume = 4/3 * (math.pi * (r**3))
    print(str(volume))


volume_ten = 10
print_volume(volume_ten)    # Input 1: calling a function with a variable
print_volume(10*2)          # Input 2: calling a function with an expression 
print_volume(10+2)          # Input 3: calling a function with an expression 

# Outputs
# 4188.79020478639     
# 33510.32163829112    
# 7238.229473870882     
    
    
    
# Question 2
def FootballStatistics(playerName, goals , assists ):
    print("\nThe total number of goals scored by " + playerName + " this year is " + str(goals) + " goals")
    print("The total number of assists given by " + playerName + " this year is " + str(assists) + " assists\n") 
    

# Input:  calling a function with multiple values/arguments     
FootballStatistics("Cristiano Ronaldo", 60, 25)   
FootballStatistics("Kylian Mbappe", 40, 10)       
FootballStatistics("Lionel Messi", 55, 35)        
FootballStatistics("Ousmane Dembele", 5, 3)        


# Outputs
# The total number of goals scored by Cristiano Ronaldo this year is 60 goals
# The total number of assists given by Cristiano Ronaldo this year is 25 assists


# The total number of goals scored by Kylian Mbappe this year is 40 goals
# The total number of assists given by Kylian Mbappe this year is 10 assists


# The total number of goals scored by Lionel Messi this year is 55 goals
# The total number of assists given by Lionel Messi this year is 35 assists   






























