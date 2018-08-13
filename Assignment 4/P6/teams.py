#! /usr/bin/python3
def makeTeams():
	while True:
		try:
			no_of_teams=input("input number of teams : ")
			no_of_players=input("input number of players : ")
			if not (no_of_players.isdigit() and no_of_teams.isdigit()):
				raise TypeError()
			no_of_teams=int(no_of_teams)
			no_of_players=int(no_of_players)
			if no_of_teams == 0 :
				raise ZeroDivisionError()
			elif no_of_players <=0 or no_of_teams <0:
				raise TypeError("Inputs must be positive")
			elif not no_of_players%no_of_teams==0:
				raise ValueError("Remove %d player(s)" % (no_of_players%no_of_teams))
			else:
				return no_of_players/no_of_teams
				exit()
		except ZeroDivisionError:
			print("number of teams must not be zero")
			continue
		except ValueError as e:
			print(str(e))
		except TypeError:
			print("Inputs must be Positive Integers")
			continue
makeTeams()