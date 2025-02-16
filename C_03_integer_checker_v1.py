
error = "please enter an integer more than / equal to 13."

while True:
    try:
        game_goal = int(input("what is the game goal"))

        if game_goal < 13:
             print(error)
        else:
            print(f"Game goal: {game_goal}")
            break

    except ValueError:
        print(error)

