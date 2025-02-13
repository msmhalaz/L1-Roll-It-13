

# check the user says yes/no
def yes_no(question):
    """Checks user response to a question is yes / no (y/n), returns 'yes' or 'no' """
    while True:
        response = input(question).lower()
        # check the user says yes / no / y / n
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes/no")
        


# Main rountine
# testing loop...
while True:
    want_instructions = yes_no("Do you want see the instructions?")
    print(f"you chose {want_instructions}")

print("we done")