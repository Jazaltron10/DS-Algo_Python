num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+ , - , * , /): ")


def calculator():
    match operation:
        case "+":
            result = num_1 + num_2
            print(f"The result is {result}")
        
        case "-":
            result = num_1 - num_2
            print(f"The result is {result}")
        
        case "*":
            result = num_1 * num_2
            print(f"The result is {result}")
        
        case "/": 
            if num_2 == 0:
                print(f"Cannot divide by zero")
            else:
                result = num_1 / num_2
                print(f"The result is {result}")
            
        case _ :
            print(f"Only numbers allowed")
    


calculator()