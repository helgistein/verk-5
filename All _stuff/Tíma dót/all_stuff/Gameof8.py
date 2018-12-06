def games_of_eights(a_list):
    prev = 0
    for number in a_list:
            number = int(number)
            if number == 8:
                if prev == 8:
                    return True
            prev = number

    return False


def main():
    a_list = input("Enter elements of list separated by commas: ").split(',')
    try:
        for number in a_list:
            number = int(number)
        value = games_of_eights(a_list)
    except ValueError:
        value = ("Error. Please enter only integers.")
    print(value)

main()