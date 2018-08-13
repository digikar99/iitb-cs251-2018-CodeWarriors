def makeTeams():
	while True:
		try:
			no_of_teams=input("input number of teams : ")
			no_of_players=input("input number of players : ")
			if no_of_teams==0:
				raise ZeroDivisionError()
			elif not no_of_players%no_of_teams==0:
				raise ValueError()
			else:
				return no_of_players/no_of_teams
				exit()
		except ZeroDivisionError:
			print("no_of_teams must be atleast once")
			continue
		except ValueError:
			print("Remove %d player(s)" % (no_of_players%no_of_teams))
			continue
makeTeams()