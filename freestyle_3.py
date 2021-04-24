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
