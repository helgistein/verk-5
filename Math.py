Max_pos = 10
Min_pos = 1
curr_pos = 0
char_movement = ''

def print_help():
    print("l - for moving left")
    print("r - for moving right")
    print("Any other letter for quitting")
    return 

def move_character(move_letter, Min_position, Max_position, curr_position):
    new_position = 0
    if move_letter == 'r' and curr_position < Max_position:
        new_position = curr_position + 1
    elif move_letter == 'r' and curr_position == Max_position:
        new_position = curr_position
    elif move_letter == 'l' and curr_position > Min_position:
        new_position = curr_position - 1
    elif move_letter == 'l' and curr_position == Min_position:
        new_position = curr_position

    return new_position

curr_pos = int(input("Input a position between 1 and 10: "))
print_help()
char_movement = input("Input your choice: ")

while char_movement == 'r' or char_movement == 'l':
    
    curr_pos = move_character(char_movement, Min_pos, Max_pos, curr_pos)
    print("New position is: {}".format(str(curr_pos)))
    print_help()
    char_movement = input("Input your choice: ")

print("New position is : {}".format(str(curr_pos)))