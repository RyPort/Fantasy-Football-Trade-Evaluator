from espn_api.football import League
from tkinter import ttk
from tkinter import *

id = 374100
year = 2020
keys = open("keys.txt","r")
id = keys.readline()
id = id[0:-1]
id = int(id)
my_swid = keys.readline()
my_swid = my_swid[0:-1]
my_s2 = keys.readline()

print(id)
print(my_swid)
print(my_s2)


league = League(league_id=id,year=year,swid=my_swid,espn_s2=my_s2)

actions = league.recent_activity(50,"TRADED")
for x in actions:
    print(x)
    print("\n")

team1 = None
team2 = None
i = 1
"""
for x in league.teams:
    print(i, end='')
    print(". ", end='')
    print(x.team_name)
    i = i+1

# Get info about the trade
team1_int = int(input("Enter corresponding number for team 1: "))
team2_int = int(input("Enter corresponding number for team 2: "))


team1 = league.teams[team1_int - 1]
team2 = league.teams[team2_int - 1]

num_team_1 = int(input("How many players did team 1 recieve in the trade? "))
num_team_2 = int(input("How many players did team 2 recieve in the trade? "))

players_team_1 = []
i = 1
print("\n")
# Get players that were traded from team 2 to team 1
for x in team1.roster:
    print(i, end ='')
    print(". ", end = '')
    print(x.name)
    i= i+1

for i in range(num_team_1):
    num = int(input("Enter corresponding number of player recieved in trade: "))
    players_team_1.append(team1.roster[num - 1])


# Get players that were traded from team 1 to team 2
players_team_2 = []
i=1
for x in team2.roster:
    print(i, end ='')
    print(". ", end = '')
    print(x.name)
    i= i+1

for i in range(num_team_2):
    num = int(input("Enter corresponding number of player recieved in trade: "))
    players_team_2.append(team2.roster[num - 1])


#print(players_team_1)   
#print(players_team_2)
#13-16
startweek = int(input("Enter the week when the trade was processed: "))
endweek = int(input("Enter the final week of the season: "))

matchup1 = None
matchup2 = None

"""
"""for i in range(startweek,endweek):
    box_scores = league.box_scores(i)
    for x in box_scores:
        if(x.home_team == team1)
"""
"""
for i in range(startWeek, endWeek):
    box_scores = league.box_scores(i)
    for x in box_scores:
        if(x.home_team == beat or x.away_team == beat):
            matchup1 = x
        if(x.home_team == herb or x.away_team == herb):
            matchup2 = x
    # have the 2 matchups that the teams were in, get player scores
    # get team lineups
    lineup1 = None
    if(matchup1.home_team == beat):
        lineup1 = matchup1.home_lineup
    else:
        lineup1 = matchup1.away_lineup
    #get 2nd team lineup
    lineup2 = None
    if(matchup2.home_team == herb):
        lineup2 = matchup2.home_lineup
    else:
        lineup2 = matchup2.away_lineup
    
    #add players score to the total
    for y in lineup1:
        if(y.name == player1):
            player2Sum += y.points
        if(y.name == player2):
            player3Sum += y.points
    
    for z in lineup2:
        if(z.name == player3):
            player1Sum += z.points
        if(z.name == player4):
            player1Sum += z.points
    """
