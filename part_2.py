# открытие файла с имеющимися играми
with open('C:\\Users\\Karonte\\Desktop\\Matches.txt') as games_basa_1:
  games_basa = list(games_basa_1)

# открытие файла с сегодняшними играми или нужными играми
with open('C:\\Users\\Karonte\\Desktop\\Games.txt') as games_today_1:
  games_today = list(games_today_1)

# перебор сегодняшних игр. срез строки так чтобы был коридор кэфа, напр. 1.5-4.0-6.0
for need_game in games_today:
  needed_odds = need_game[26:40]
  need_odd = f"{needed_odds[0:3]}-{needed_odds[5:8]}-{needed_odds[10:13]}"

  # для каждой сегодняшней игры перебор уже имеющихся игр. в том же формате 1.4-4.5-7.7
  for match in games_basa:
    odds = match[26:40]
    searching_odd = f"{odds[0:3]}-{odds[5:8]}-{odds[10:13]}"

    # если коридоры совпали то вывод на экран
    if need_odd == searching_odd:
      print(match.upper(), need_game)
