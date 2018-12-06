def mutate_list(a_list, index_num, v):
    ''' Inserts v at index index_num in a_list'''
    a_list.insert(index_num, v)
    
def remove_ch(a_list, index_num):
    ''' Removes character at index_num from a_list'''
    a_list.pop(index_num)
    
def get_list():
    ''' Reads in values for a list and returns the list '''
    user_list = input("Enter values in list separated by commas: ")
    user_list = user_list.split(",")
    user_list = [int(i) for i in user_list]
    return user_list

# Main program starts here

new_list = get_list()
print(new_list)
user_choice = input("Enter choice (m,r): ")

if user_choice == "r":
    remove_nr = int(input())
    remove_ch(new_list, remove_nr)
    print(new_list)

elif user_choice == "m":
    change_nr,to_nr = input().split(',')
    mutate_list(new_list, int(change_nr), int(to_nr))
    print(new_list)

else:
    print(new_list)