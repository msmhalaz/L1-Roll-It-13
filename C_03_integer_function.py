
def int_check():
    """Check users enter an integer more than / equal to 13"""

    error = "please enter an integer more than / equal to 13."

    while True:
        try:
            response = int(input("what is the game goal"))

            if response < 13:
                 print(error)
            else:
               return response
        except ValueError:
            print(error)


# main routine starts here
game_goal = int_check()
print(game_goal)

