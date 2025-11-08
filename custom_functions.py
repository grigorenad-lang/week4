# custom_functions.py
# This program defines a function to simulate hearing a sound in a cave.
# The function 'listen' asks the user to enter a sound and responds with a message.

def listen():
    """
    Prompts the user to input a sound and then displays a message
    indicating that the sound was loud.
    """
    # Ask the user to input a sound
    sound = input("What sound did you hear?\n")

    # Display the message with the entered sound
    print(f"\nThat was a loud {sound}!")


# Call the listen function
listen()