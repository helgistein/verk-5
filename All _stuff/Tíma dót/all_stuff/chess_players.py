RANK = 0
NAME = 1
COUNTRY = 2
POINTS = 3
YEAR = 4

def get_input(user_prompt):
    user_input = input(user_prompt)
    return user_input
    
def read_file(file_name):
    try:
        file_content = open(file_name, "r")
        return file_content
    except FileNotFoundError:
        return None

def create_key(data_list):
    last_name, first_name = data_list.split(",")
    last_name = last_name.strip()
    first_name = first_name.strip()
    return "{} {}". format(first_name, last_name)


def clean_data(data_list):
    
    country = data_list[COUNTRY].strip()
    points = int(data_list[POINTS].strip()) 
    birth_year = int(data_list[YEAR].strip())
    rank = (data_list[RANK].strip)
    return [rank, country, points, birth_year]


def create_dict_from_file_data(file_content):
    chess_players_dict = {}
    for data in file_content:
        data = data.split(";")
        key = create_key(data[NAME])
        chess_players_dict[key] = clean_data(data)

    return chess_players_dict

def get_points_per_country(chess_players_dict):
    my_dict = {}
    for chess_players_dict in chess_players_dict.items():
        country = chess_players_dict[1][1]
        if country in my_dict:
            my_dict[country][0] += 1
            my_dict[country][1] += chess_players_dict[1][2]
        else:
            data = [1, chess_players_dict[1][2]]
            my_dict[country] = data
    return my_dict

def print_header(header_str):
    print(header_str)
    print("-" * len(header_str))

def print_results(chess_players_dict, countries_dict):
    for country in sorted(countries_dict.keys()):
        number_of_players = countries_dict[country][0]
        total_points = countries_dict[country][1]
        average = total_points / number_of_players
        print("{} ({}) ({:.1f}):".format(country, number_of_players, average))
        for player in chess_players_dict.keys():
            if chess_players_dict[player][1] == country:
                print("{:>40}{:>10d}".format(player, chess_players_dict[player][2]))

def main():
    #get name of file
    file_name = get_input("Enter filename: ")
    #get data from csv file
    file_content = read_file(file_name)
    
    if file_content:
        #Create dictionary from csv data, key=name
        chess_players_dict = create_dict_from_file_data(file_content)
        file_content.close
        #calculate average for each country
        countries_dict = get_points_per_country(chess_players_dict)
        #calculate number of players for each country
        #print results in a formatted manner
        print_header("Players by country")
        print_results(chess_players_dict, countries_dict)



main()