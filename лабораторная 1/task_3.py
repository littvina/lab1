list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
kolvo = len(list_players)
f_com = list_players[:int(kolvo/2)]
s_com = list_players[int(kolvo/2):]
print(f_com)
print(s_com)
