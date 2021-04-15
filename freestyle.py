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

def clear():
    print("Calling clearScreen()")
    new_line()
    three_lines()
    three_lines()
    nine_lines()
    nine_lines()
    
print("Printing Nine lines")    
nine_lines()
#clear()
# nine_lines()    
# nine_lines()    
# nine_lines()    
    
    
    
pi = 3.142

def print_volume(r):
    return 4/3*(pi*(r**3))
    

volume_four = 4
print(print_volume(5))
print(print_volume(volume_four))
print(f"The volume of the sphere of radius 9 is {print_volume(9)}")




def i_will_take_your_arguments(name):
    print("Hello "+ name)
    

my_name = "King Jasper"
i_will_take_your_arguments("john")
i_will_take_your_arguments(my_name)
i_will_take_your_arguments("john's King")



def Local_variable_function():
    name = "Jesse"
    age = 19
    
print(20 + age)    




def Example_4(parameter_unique):
    return parameter_unique + 20
    
print(Example_4(30))
print(parameter_unique + 50)    
    
    


goals = 30   
def Example_5():
    goals = 90
    print(f"The total amount of goals scored this year by Ronaldo is {goals}")
    
Example_5()    






































