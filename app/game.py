import random
from innings import Innings
from team import Team
import os

team1 = Team(input("gib team 1 name: "))
team2 = Team(input("gib team 2 name: "))
os.system("cls")
print(team1.team_name)
print()
print(team1.squad)
print()
print(team2.team_name)
print()
print(team2.squad)
innings = Innings(team1, team2)
innings.play() 
