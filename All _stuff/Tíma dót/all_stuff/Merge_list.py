def merge_lists(list1, list2):
    merge_lists = (list1 + list2)
    new_list = []
    for i in merge_lists:
        if i not in new_list:
            new_list.append(i)


    new_list.sort()
    return new_list

# Main program starts here - DO NOT change it
list1 = input("Enter elements of list separated by commas: ").split(',')
list2 = input("Enter elements of list separated by commas: ").split(',')
print(merge_lists(list1, list2))