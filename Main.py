# Tayler Rae Bachmann
# This program allows two players to play Tic-Tac-Toe. At the end is also a
# skippable math portion


# The game_board() function will print the modified game board when it is
# called, every player move will readjust the game board with the new X or 0
# placement. This function will be called after each player's moves to
# show the current placements and available spots
def game_board():
    print(gb_line_one[0], gb_line_one[1], gb_line_one[2])
    print(horizontal_line)
    print(gb_line_two[0], gb_line_two[1], gb_line_two[2])
    print(horizontal_line)
    print(gb_line_three[0], gb_line_three[1], gb_line_three[2])
    print()


# The test_win_p1() function tests if Player One (X) won or not. P1 stands for
# 'Player One'. Each if and elif statement tests a different row/column for
# three X's. For example, if row one has " X  |" in each spot [0], [1],
# and [2] then it will print the string "Player One wins!", print the new game
# board and quit the program, ending the game. This functions tests all three
# rows, all three columns, and both diagonals. If all of the if and elif
# statements are false and Player One does not win, the else statement
# prints the modified game board and it continues to Player Two's next turn
def test_win_p1():
    if gb_line_one == [" X  |", " X  |", " X  |"]:
        print("Player One wins!")
        game_board()
        quit()
    elif gb_line_two == [" X  |", " X  |", " X  |"]:
        print("Player One wins!")
        game_board()
        quit()
    elif gb_line_three == [" X  |", " X  |", " X  |"]:
        print("Player One wins!")
        game_board()
        quit()
    elif gb_line_one[0] == " X  |" and gb_line_two[0] == " X  |" \
            and gb_line_three[0] == " X  |":
        print("Player One wins!")
        game_board()
        quit()
    elif gb_line_one[1] == " X  |" and gb_line_two[1] == " X  |" \
            and gb_line_three[1] == " X  |":
        print("Player One wins!")
        game_board()
        quit()
    elif gb_line_one[2] == " X  |" and gb_line_two[2] == " X  |" \
            and gb_line_three[2] == " X  |":
        print("Player One wins!")
        game_board()
        quit()
    elif gb_line_one[0] == " X  |" and gb_line_two[1] == " X  |" \
            and gb_line_three[2] == " X  |":
        print("Player One wins!")
        game_board()
        quit()
    elif gb_line_one[2] == " X  |" and gb_line_two[1] == " X  |" \
            and gb_line_three[0] == " X  |":
        print("Player One wins!")
        game_board()
        quit()
    else:
        game_board()


# The test_win_p2() function tests if Player Two (0) won or not. P2 stands for
# 'Player Two'. Each if and elif statement tests a different row/column for
# three 0's. For example, if row one has " 0  |" in each spot [0], [1],
# and [2] then it will print the string "Player Two wins!", print the new game
# # board and quit the program, ending the game. This functions tests all
# three rows, all three columns, and both diagonals. If all of the if and
# elif statements are false and Player Two does not win, the else statement
# prints the modified game board and it continues to Player One's next turn
def test_win_p2():
    if gb_line_one == [" 0  |", " 0  |", " 0  |"]:
        print("Player Two wins!")
        game_board()
        quit()
    elif gb_line_two == [" 0  |", " 0  |", " 0  |"]:
        print("Player Two wins!")
        game_board()
        quit()
    elif gb_line_three == [" 0  |", " 0  |", " 0  |"]:
        print("Player Two wins!")
        game_board()
        quit()
    elif gb_line_one[0] == " 0  |" and gb_line_two[0] == " 0  |" \
            and gb_line_three[0] == " 0  |":
        print("Player Two wins!")
        game_board()
        quit()
    elif gb_line_one[1] == " 0  |" and gb_line_two[1] == " 0  |" \
            and gb_line_three[1] == " 0  |":
        print("Player Two wins!")
        game_board()
        quit()
    elif gb_line_one[2] == " 0  |" and gb_line_two[2] == " 0  |" \
            and gb_line_three[2] == " 0  |":
        print("Player Two wins!")
        game_board()
        quit()
    elif gb_line_one[0] == " 0  |" and gb_line_two[1] == " 0  |" \
            and gb_line_three[2] == " 0  |":
        print("Player Two wins!")
        game_board()
        quit()
    elif gb_line_one[2] == " 0  |" and gb_line_two[1] == " 0  |" \
            and gb_line_three[0] == " 0  |":
        print("Player Two wins!")
        game_board()
        quit()
    else:
        game_board()


# These variables initialize the lists used to make the game board and a
# horizontal line to seperate the rows to make it visually better for the
# players/users. 'gb' stands for 'game board'. Each index for each line has
# a number 1-9 so when the player's are choosing their spot they can choose
# a number and that spot will be replaced with an X or 0 depending on which
# player chose that spot
gb_line_one = ["  1  |", " 2  |", " 3  "]
gb_line_two = ["  4  |", " 5  |", " 6  "]
gb_line_three = ["  7  |", " 8  |", " 9  "]
horizontal_line = "----- " * 3

# This list will act as a way to keep track of which spots had already been
# taken so one player can not overwrite the moves of a previous player and
# only empty spots can be claimed. 'prev' stands for 'previous'.
prev_moves = []

# This is an introduction to the players and will call the game_board()
# function so the players can see the spots 1-9. This part also designates
# Player One as X and Player 2 as 0
print("Let's play Tic-Tac-Toe!")
print("Player One will be X and Player Two will be 0")
print("Here's your board!", end=' ')
print("Each number 1-9 represents a space on the board", )
game_board()

# This is Player One's first move. 'p1' stands for 'Player One' and 'm1'
# stands for 'move one' so together the variable 'p1_m1' stands for Player
# One's move one. It  starts with asking for Player One to choose a spot
# from the board 1-9. The first while loop checks if the user picked a spot
# 1-9, if they did not it will ask them to pick a new number 1-9 until they
# do. Once they pick a valid number it will add that spot number into the
# previous moves list so it can not be chosen later on. Then if Player One
# move one was 1-3 it will become the new value in the respective index spot
# in game board line one. If the move was 4-6 it will go into game board
# line two. If the move was 7-9 it will go into the game board line three.
# At the end of filling the chosen spot it calls the test_win_p1() function
# and then moves onto player two's move
p1_m1 = int(input("Player One, please choose which spot "
                  "you would like:"))
while p1_m1 not in range(1, 10):
    p1_m1 = int(input("Please choose a spot from 1-9:"))
for p1_m1 in prev_moves:
    p1_m1 = int(input("That spot has already been chosen, "
                      "please pick a different spot:"))
prev_moves.append(p1_m1)
print()

if p1_m1 in range(1, 4):
    gb_line_one[p1_m1 - 1] = " X  |"
elif p1_m1 in range(4, 7):
    gb_line_two[p1_m1 - 4] = " X  |"
elif p1_m1 in range(7, 10):
    gb_line_three[p1_m1 - 7] = " X  |"
test_win_p1()

# This is Player Two's first move. 'p2' stands for 'Player Two' and 'm1'
# stands for 'move one' This section works the same as the other player
# moves sections
p2_m1 = int(input("Player Two, please choose which spot "
                  "you would like:"))
while p2_m1 not in range(1, 10):
    p2_m1 = int(input("Please choose a spot from 1-9:"))
for p2_m1 in prev_moves:
    p2_m1 = int(input("That spot has already been chosen, "
                      "please pick a different spot:"))
prev_moves.append(p2_m1)
print()

if p2_m1 in range(1, 4):
    gb_line_one[p2_m1 - 1] = " 0  |"
elif p2_m1 in range(4, 7):
    gb_line_two[p2_m1 - 4] = " 0  |"
elif p2_m1 in range(7, 10):
    gb_line_three[p2_m1 - 7] = " 0  |"
test_win_p2()

# This is Player One's second move. This section works the same as the other
# player moves sections
p1_m2 = int(input("Player One, please choose which spot "
                  "you would like:"))
while p1_m2 not in range(1, 10):
    p1_m2 = int(input("Please choose a spot from 1-9:"))
for p1_m2 in prev_moves:
    p1_m2 = int(input("That spot has already been chosen, "
                      "please pick a different spot:"))
prev_moves.append(p1_m2)
print()

if p1_m2 in range(1, 4):
    gb_line_one[p1_m2 - 1] = " X  |"
elif p1_m2 in range(4, 7):
    gb_line_two[p1_m2 - 4] = " X  |"
elif p1_m2 in range(7, 10):
    gb_line_three[p1_m2 - 7] = " X  |"
test_win_p1()

# This is Player Two's second move. This section works the same as the other
# player moves sections
p2_m2 = int(input("Player Two, please choose which spot "
                  "you would like:"))
while p2_m2 not in range(1, 10):
    p2_m2 = int(input("Please choose a spot from 1-9:"))
for p2_m2 in prev_moves:
    p2_m2 = int(input("That spot has already been chosen, "
                      "please pick a different spot:"))
prev_moves.append(p2_m2)
print()

if p2_m2 in range(1, 4):
    gb_line_one[p2_m2 - 1] = " 0  |"
elif p2_m2 in range(4, 7):
    gb_line_two[p2_m2 - 4] = " 0  |"
elif p2_m2 in range(7, 10):
    gb_line_three[p2_m2 - 7] = " 0  |"
test_win_p2()

# This is Player One's third move. This section works the same as the other
# player moves sections
p1_m3 = int(input("Player One, please choose which spot "
                  "you would like:"))
while p1_m3 not in range(1, 10):
    p1_m3 = int(input("Please choose a spot from 1-9:"))
for p1_m3 in prev_moves:
    p1_m3 = int(input("That spot has already been chosen, "
                      "please pick a different spot:"))
prev_moves.append(p1_m3)
print()

if p1_m3 in range(1, 4):
    gb_line_one[p1_m3 - 1] = " X  |"
elif p1_m3 in range(4, 7):
    gb_line_two[p1_m3 - 4] = " X  |"
elif p1_m3 in range(7, 10):
    gb_line_three[p1_m3 - 7] = " X  |"
test_win_p1()

# This is Player Two's third move. This section works the same as the other
# player moves sections
p2_m3 = int(input("Player Two, please choose which spot "
                  "you would like:"))
while p2_m3 not in range(1, 10):
    p2_m3 = int(input("Please choose a spot from 1-9:"))
for p2_m3 in prev_moves:
    p2_m3 = int(input("That spot has already been chosen, "
                      "please pick a different spot:"))
prev_moves.append(p2_m3)
print()

if p2_m3 in range(1, 4):
    gb_line_one[p2_m3 - 1] = " 0  |"
elif p2_m3 in range(4, 7):
    gb_line_two[p2_m3 - 4] = " 0  |"
elif p2_m3 in range(7, 10):
    gb_line_three[p2_m3 - 7] = " 0  |"
test_win_p2()

# This is Player One's fourth move. This section works the same as the other
# player moves sections
p1_m4 = int(input("Player One, please choose which spot "
                  "you would like:"))
while p1_m4 not in range(1, 10):
    p1_m4 = int(input("Please choose a spot from 1-9:"))
for p1_m4 in prev_moves:
    p1_m4 = int(input("That spot has already been chosen, "
                      "please pick a different spot:"))
prev_moves.append(p1_m4)
print()

if p1_m4 in range(1, 4):
    gb_line_one[p1_m4 - 1] = " X  |"
elif p1_m4 in range(4, 7):
    gb_line_two[p1_m4 - 4] = " X  |"
elif p1_m4 in range(7, 10):
    gb_line_three[p1_m4 - 7] = " X  |"
test_win_p1()

# This is Player Two's fourth move. This section works the same as the other
# player moves sections
p2_m4 = int(input("Player Two, please choose which spot "
                  "you would like:"))
while p2_m4 not in range(1, 10):
    p2_m4 = int(input("Please choose a spot from 1-9:"))
for p2_m4 in prev_moves:
    p2_m4 = int(input("That spot has already been chosen, "
                      "please pick a different spot:"))
prev_moves.append(p2_m4)
print()

if p2_m4 in range(1, 4):
    gb_line_one[p2_m4 - 1] = " 0  |"
elif p2_m4 in range(4, 7):
    gb_line_two[p2_m4 - 4] = " 0  |"
elif p2_m4 in range(7, 10):
    gb_line_three[p2_m4 - 7] = " 0  |"
test_win_p2()

# This is Player One's fifth move. This section works the same as the other
# player moves sections
p1_m5 = int(input("Player One, please choose which spot "
                  "you would like:"))
while p1_m5 not in range(1, 10):
    p1_m5 = int(input("Please choose a spot from 1-9:"))
for p1_m5 in prev_moves:
    p1_m5 = int(input("That spot has already been chosen, "
                      "please pick a different spot:"))
prev_moves.append(p1_m5)
print()

if p1_m5 in range(1, 4):
    gb_line_one[p1_m5 - 1] = " X  |"
elif p1_m5 in range(4, 7):
    gb_line_two[p1_m5 - 4] = " X  |"
elif p1_m5 in range(7, 10):
    gb_line_three[p1_m5 - 7] = " X  |"
test_win_p1()

# If none of the players win and the game board is full then it'll print
# "It's a tie!"
print("It's a tie!")

# This section is the skippable math homework portion
skip_math = input("Do you need help with your math homework?")
while skip_math != "yes" and skip_math != "no":
    print("Please only respond with a 'yes' or 'no'")
    skip_math = input("Do you need help with your math homework?")
# In these sections I will be using remainders, multiplication,
# division, and exponents
if skip_math == 'yes':
    remain_first_num = int(input("Looks like you're working with remainders, "
                                 "go ahead and input the first number:"))
    remain_second_num = int(input("Great! Now input the number you want"
                                  " divide the first number by:"))
    remain_total = remain_first_num % remain_second_num
    print("Looks like the remainder of,", remain_first_num,
          "when evenly divided by,", remain_second_num, "is:",
          remain_total)
    print("Now we can do some more advanced math, like exponents!")
    exponent_first_num = int(input("Go ahead and input the number you'd "
                                   "like to be raised:"))
    exponent_second_num = int(input("Now input the number you'd like to "
                                    "raise the first number by:"))
    exponent_third_num = int(input("And finally, input the number you'd"
                                   " like to raise the previous equation by:"))
    exponent_total = (exponent_first_num ** exponent_second_num) ** \
                     exponent_third_num
    print("So the total of", exponent_first_num, "to the power of",
          exponent_second_num, "and then that to the power of,",
          exponent_third_num, "is:", exponent_total)
    print("Now we can help with multiplication and division!")
    multi_first_num = int(input("Go ahead and input the first number you'd "
                                "like multiplied:"))
    multi_second_num = int(input("Now input the second number you'd like "
                                 "multiplied:"))
    multi_third_num = int(input("And input the third number you'd like "
                                "multiplied:"))
    divide_first_num = int(input("Finally, input the number you'd like the "
                                 "whole thing to be divided by:"))
    total_multi_divide = (multi_first_num * multi_second_num *
                          multi_third_num) / divide_first_num
    print("So when", multi_first_num, "is multiplied by", multi_second_num,
          "and", multi_third_num, "and then the whole thing is divded by",
          divide_first_num, "you get:", total_multi_divide)
else:
    print("No problem!")
