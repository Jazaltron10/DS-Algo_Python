def mad_libs():
    # Asking for user input
    adjective1 = input("Enter an adjective: ")
    adjective2 = input("Enter another adjective: ")
    adjective3 = input("Enter one more adjective: ")
    noun = input("Enter a noun: ")

    # Constructing the story with user inputs
    story = (
        f"On a beautiful {adjective1} day, I went to the zoo. "
        f"I saw a funny {adjective2} monkey swinging from the trees. "
        f"Then, I spotted a majestic {adjective3} {noun} lounging in the sun. "
        "What a wild and wonderful experience!"
    )

    # Printing the final story
    print(story)

# Calling the mad_libs function to run the program
mad_libs()
