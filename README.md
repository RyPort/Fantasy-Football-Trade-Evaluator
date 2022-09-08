# Fantasy-Football-Trade-Evaluator
### What is this project?
This project uses the ESPN fantasy python API ([here](https://github.com/cwendt94/espn-api)) to get data from any ESPN fantasy league. This data is used to find any trades that occurred throughout the season and see which team's players scored more points after the trade.

----
### Getting Started
##### Getting API keys

 1. Create a file called keys.txt in the root directory of the repo
 2. Log in to any ESPN fantasy league
 3. Copy the leagueId from the address bar into the keys.txt file 
 4. Right click > Inspect > Storage
 5. Copy your SWID from espnAuth with the brackets into keys.txt
 6. Copy espn_s2 into keys.txt
 7. Make sure keys are on their own line as shown below
 ```
leagueId
{SWID}
espn_s2 
 ```
 *User credentials are required to use this script even if the league is public
 ##### Using the Script
 `python fantasy.py`
 All of the league's trades will be printed to the console as shown below. Just type the number of the trade that you want to evaluate and all the corresponding player/team trade info will be printed to the console.
 ![Example Trades](https://i.imgur.com/uGHOVEl.png)
 ### Limitations
 
 - The API has an unknown daily/hourly limit
 - The API is no officially supported by ESPN

