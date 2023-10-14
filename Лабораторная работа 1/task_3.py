list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]


all_players = len(list_players)
middle_list_index = all_players // 2
team1 = list_players[:middle_list_index]
team2 = list_players[middle_list_index:]

print(team1, team2, sep='\n')