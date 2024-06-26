task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            reminder = f"'{task}' is a high priority task that requires immediate attention today!"
            # print(f"{task} is a {priority} priority task that requires immediate action today!")
        else:
            reminder = f"'{task}' is a high priority task."
    case "medium":
        if time_bound == "yes":
            reminder = f"'{task}' is a medium priority task that requires immediate attention today!"
            # print(f"{task} is a {priority} priority task that requires immediate action today!")
        else:
            reminder = f"'{task}' is a medium priority task."
    case "low":
        if time_bound == "yes":
            reminder = f"'{task}' is a low priority task that requires immediate attention today!"
            # print(f"{task} is a {priority} priority task that requires immediate action today!")
        else:
            reminder = f"'{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority level. Please enter high, medium, or low."

print("Reminder:", reminder)