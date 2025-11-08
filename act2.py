# custom_functions.py
# Text adventure helpers: listen, identify, escape_by

def listen():
    """
    Ask the user for a sound and report it back loudly.
    """
    sound = input("What sound did you hear?\n")
    print(f"\nThat was a loud {sound}!")


def identify():
    """
    Ask what lies ahead and advise if it's a large boulder.
    """
    sight = input("What lies before us?\n")
    if sight.strip().lower() == "a large boulder":
        print("\nIt's time to run!")
    else:
        print("\nWe will be fine.")


def escape_by(plan):
    """
    Decide if a given escape plan will work.
    """
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is too big!")
    elif plan == "running around":
        print("We cannot escape that way! The boulder is moving too fast!")
    elif plan == "cross bridge ahead":
        print("That might just work! Let's go!")
    else:
        print("We cannot escape that way! The boulder is in the way!")


# Only auto-run the required escape tests.
# (The input-based functions are left commented so the script doesn't pause.)
if escape_by() plan == "_main_":
    escape_by("jumping over")
    escape_by("running around")
    escape_by("cross bridge ahead")
    # To test these interactively, uncomment:
    # listen()
    # identify()
