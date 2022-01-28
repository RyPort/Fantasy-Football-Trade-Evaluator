from espn_api.football import League
from espn_api.football import Matchup

id = 374100
year = 2020
#print(league.teams)
keys = open("keys.txt","r")

my_swid = keys.readline()
my_swid = my_swid[0:-1]
my_s2 = keys.readline()
league = League(league_id=id,year=year,swid=my_swid,espn_s2=my_s2)
act = league.recent_activity(25,'TRADED')

# players that team1 and team2 traded away respectively
players_team1 = []
players_team2 = []

# Gets player score for specified week
def getPlayerScore(name:str, week:int):
    # search for player name in given week
    sb = league.box_scores(week)
    # search home team roster
    for score in sb:
        for player in score.home_lineup:
            if player.name == name:
                return player.points
        for player in score.away_lineup:
            if player.name == name:
                return player.points
    return 0
def printTrades():
    num_trade = 1
    for trade in act:
        print(str(num_trade) + '. ')
        num_trade +=1
        # add team and player names to string list to make it easier to read
        # get the team names
        team1 = None
        team2 = None
        for item in trade.actions:
            if team1 == None:
                team1=item[0]
            elif team2 == None and team1 != item[0]:
                team2=item[0]
        # print players from team 1
        print(team1.team_name+": ")
        for item in trade.actions:
            if item[0] == team1:
                print(item[2].name+', ')
        print()
        print(team2.team_name+': ')
        for item in trade.actions:
            if item[0] == team2:
                print(item[2].name+', ') 
        
        print()
# populates player lists for the teams involved in the trade
# returns a list with the 2 Team objects    
def getTradeData():
    trade_selection = int(input('Select a trade to evaluate: '))
    # get player names from trade
    transaction = act[trade_selection-1]
    team_list = []
    team1 = None
    team2 = None
    for item in transaction.actions:
        if team1 == None:
            team1=item[0]
        elif team2 == None and team1 != item[0]:
            team2 = item[0]
        if item[0] == team1:
            players_team1.append(item[2])
        else:
            players_team2.append(item[2])
    team_list.append(team1)
    team_list.append(team2)
    return team_list
# search team rosters and find week where player first appears
# param is any player involved in the trade and the team they were traded to
def getTradeWeek(player_name, player_new_team):
    for i in range(1,17):
        for box_score in league.box_scores(i):
            if box_score.home_team == player_new_team:
                for player in box_score.home_lineup:
                    if player.name == player_name:
                        return i
            elif box_score.away_team == player_new_team:
                for player in box_score.away_lineup:
                    if player.name == player_name:
                        return i


#print(getPlayerScore('Josh Jacobs', 2))

printTrades()
teams = getTradeData()
team1 = teams[0]
team2 = teams[1]
trade_week = getTradeWeek(players_team2[0].name,team1)

# display player totals for team 1
print(team1.team_name)
team1_total = 0
for player in players_team2:
    sum = 0
    for i in range(trade_week,17):
        sum += getPlayerScore(player.name, i)
    print(player.name+': '+str(sum))
    team1_total+=sum
print('The players '+team1.team_name+' received in the trade scored '+str(team1_total)+' points after the trade was completed')
print()
print(team2.team_name)
team2_total = 0
for player in players_team1:
    sum = 0
    for i in range(trade_week,17):
        sum += getPlayerScore(player.name, i)
    print(player.name+': '+str(sum))
    team2_total += sum
print('The players '+team2.team_name+' received in the trade scored '+str(team2_total)+' points after the trade was completed')





