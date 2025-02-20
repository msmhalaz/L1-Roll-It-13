import random


def initial_points(which_player):
    """Roll dice twice and return total / if double points apply"""

    double = "no"

    # Roll the dice for the user and note if they got a double
    roll_one = random.randint(1, 6)
    roll_two = random.randint(1, 6)

    if roll_one == roll_two:
        double = "yes"

    total = roll_one + roll_two
    print(f"{which_player} - Roll 1: {roll_one} \t| Roll2: {roll_two} \t| Total: {total}")

    return total, double

# Main starts here...


# Roll the dice for the user and note if they got a double
initial_user = initial_points("User")
initial_comp = initial_points("Comp")



# Retrieve user points (first item returned from function)
user_points = initial_user[0]
comp_points = initial_comp[0]

double_user = initial_user[1]

# Let the user know if they qualify for double points
  if double_user == "yes":
   print("Great news = if you win, you will earn double points!")

# assume user goes first...
first = "User"
second = "Computer"
player_1_points = user_points
player_2_points = comp_points


# if user has fewer points, they start the game
if user_points < comp_points:
    print("you start because your initial roll was less than the computer\n")

# if the user and computer roll equal points, the users is player 1...
elif user_points == comp_points:
    print("The initial rolls were the same, the user starts!")

# if the computer has fewer points, switch the computer to 'player 1'
else:
    player_1_points, player_2_points = player_2_points, player_1_points
    first, second = second, first

    # Loop until we have a winner...
while player_1_points < 13 and player_2_points < 13:
    print()
    input("press <enter> to continue this round\n")

    # first person rolls the dice and score is updated
    player_1_roll = random.randint(1, 6)
    player_1_points += player_1_roll

    print(f"{second}: Rolled a {player_2_roll} - has {player_2_points} points")

    # if the first person's score is over 13, end the round
    if player_1_points >= 13:
        break

        #second person rolls the dice (and score is updated)
        player_2_roll = random.randint (1, 6)
        player_2_points += player_2_roll

        print(f"{second}: Rolled a {player_2_roll} - has {player_2_points} points")

        print(f"{first}: {player_1_points} | {second} {player_2_points}")

        print("end of round")


