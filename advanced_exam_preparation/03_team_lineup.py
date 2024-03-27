def team_lineup(*args):
    new_dict = {}
    for player in args:
        name = player[0]
        country = player[1]
        if country not in new_dict:
            new_dict[country] = []
        new_dict[country].append(name)

    new_dict = dict(sorted(new_dict.items(), key=lambda x: (- len(x[1]), x[0])))

    result = ''
    for country, player_names in new_dict.items():
        result += f'{country}:\n'

        for player in player_names:
            result += f"  -{player}\n"

    return result


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))



