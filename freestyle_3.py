calculation_to_secs = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_secs} {name_of_unit}"
        
            



def validate_and_execute():
    try:
        User_input_number = int(num_of_days_element)
        
        # we want to do conversion only for positive integers
        if User_input_number > 0:
            Calculated_Value = days_to_units(User_input_number)
            print(Calculated_Value)
        elif User_input_number == 0:
            print("You entered a 0, please enter a valid positive number")
        else:
            print("You entered a negative number, no conversion for you!")
    except ValueError:
        print("Your input is not a valid number, Don't ruin my program!")



User_input = ""
while User_input != "exit":
    User_input = input("Hey user, enter a number of days as a space separated list and i will convert it to hours!\n")
    list_of_days = User_input.split(" ")

    print(list_of_days)
    print(set(list_of_days))

    print(type(list_of_days))
    print(type(set(list_of_days)))

    for num_of_days_element in set(list_of_days):
        print(num_of_days_element*2)
        validate_and_execute()