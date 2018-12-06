
def get_list():
    a_list = input("Enter elements of list separated by commas: ").strip().split(',')
    return a_list
def even_sum(a_list):
    int_list = [int(x) for x in a_list ]
    return sum([x for x in int_list if x % 2 == 0])


# Main program starts here - DO NOT change it
a_list = get_list()
print(even_sum(a_list)) 
