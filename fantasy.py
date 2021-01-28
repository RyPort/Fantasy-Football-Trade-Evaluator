from espn_api.football import League

id = 374100
year = 2020
league = League(league_id=id,year=year,swid="{E3ED957C-6A4E-4F78-B94B-465E9D885563}",espn_s2="AEAeTVHJx6ryMDMAUly4pkh9IC2dQqYR%2FnebCuQdaSmCFiMAbfNk0og14KceNh7BI6%2B4O4X98t6qM0fsZpQsYJIrUS5UutZUWhPOsQU1fDz17eC7BS8IvZ9FDAbfyAiqtcRJFzsIy4ucsjA%2BC2Q7FA2zh09Hik14Ihafb4%2FYEE%2ByiBE2Hc%2FUgGnk7Ewc9XOmvife1zhqaH6eXSCGFideIlSywWSkjvVrneyBQyCkTtDRDUS0k%2BFrTamr3TncP6HfM%2Fa%2BEbqrMiC7CTwCeCNpCoI1")
#print(league.teams)
beat = league.teams[4]
herb = league.teams[3]
startWeek = 13
endWeek = 16
player1 = "Travis Kelce"
player2 = "Justin Jefferson"
player3 = "Darren Waller"
player4 = "Christian McCaffrey"

player1Sum = 0.0
player2Sum = 0.0
player3Sum = 0.0
player4Sum = 0.0


matchup1 = None
matchup2 = None

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
    
print(player1, end=" ")
print(player1Sum)
print(player2, end=" ")
print(player2Sum)
print(player3, end=" ")
print(player3Sum)
print(player4, end=" ")
print(player4Sum)





