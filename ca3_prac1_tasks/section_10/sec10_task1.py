def compare(input1, input2):
    choices = ["scissors", "paper", "stone", "quit"]

    if input1 == "quit" or input2 == "quit":
        return "Quitting the program...", True

    if input1 not in choices or input2 not in choices:
        return "Invalid input. Please try again", False

    if input1 == input2:
        return "It’s a tie", False

    if input1 == "scissors" and input2 == "paper":
        return "Scissors wins!", False

    if input1 == "scissors" and input2 == "stone":
        return "Stone wins!", False

    if input1 == "paper" and input2 == "scissors":
        return "Scissors wins!", False

    if input1 == "paper" and input2 == "stone":
        return "Paper wins!", False

    if input1 == "stone" and input2 == "scissors":
        return "Stone wins!", False

    if input1 == "stone" and input2 == "paper":
        return "Paper wins!", False


player1 = input("Enter name of Player 1: ")
player2 = input("Enter name of Player 2: ")

quit_game = False
while quit_game is False:
    print()
    player1_input = input("{}, please choose Scissors, Paper or Stone: ".format(player1)).lower()
    player2_input = input("{}, please choose Scissors, Paper or Stone: ".format(player2)).lower()

    result, quit_game = compare(player1_input, player2_input)
    print(result)
