from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    Current_date = datetime.today()
    print(f"Current date and time: {Current_date.replace(microsecond=0)}")
    
display_current_datetime()
    
# Part 2: Calculate a Future Date
def calculate_future_date():
    number_of_days = int(input("\nEnter the number of days to add to the current date: "))
    today_date = datetime.now()
    Future_date = today_date + timedelta(days=number_of_days)
    print(f"Future date: {aFuture_date.strftime('%Y-%m-%d')}")
    
calculate_future_date()