# custom_functions.py
# This program simulates a text-based adventure game with functions
# to respond to user input based on what they hear or see.

def listen():
    """
    Prompts the user to input a sound and then displays a message
    indicating that the sound was loud.
    """
    # Ask the user to input a sound
    sound = input("What sound did you hear?\n")

    # Display the message with the entered sound
    print(f"\nThat was a loud {sound}!")


def identify():
    """
    Prompts the user to input what they see and responds based
    on whether it's a large boulder or something else.
    """
    # Ask the user to input what they see
    sight = input("What lies before us?\n")

    # Check the user's response and display appropriate message
    if sight.lower() == "a large boulder":
        print("\nIt's time to run!")
    else:
        print("\nWe will be fine.")


# Call the functions to test them
# Comment out one of the calls if you only want to test one at a time
# listen()
identify()