from django.shortcuts import render
from django.http import HttpResponse
import datetime
import ssl
from urllib import request
import xml.etree.ElementTree as ET

#Variables
api_key = "437f94816cda4083bd6b4d276d4028f6"
#from first_project import ScrapeData.py

def scrape_mlb(date):
    url = "https://api.sportsdata.io/v3/mlb/odds/xml/LiveGameOddsByDate/" + date + "?key=" + api_key
    raw_data = request.urlopen(url, context=ssl._create_unverified_context())
    tree = ET.parse(raw_data)
    root = tree.getroot()

    #Variable to hold all games
    games = []

    #Goes through each root and creates a game object and adds it to the list
    for i in range(len(root)):
        games.append(Game(root[i][0].text, "mlb", root[i][4].text, root[i][5].text, root[i][8].text, root[i][9].text, root[i][16].text, root[i][17].text))

    return games

    #Game(root[0][0].text, "mlb", root[0][4].text, root[0][5].text, root[0][8].text, root[0][9].text, root[0][16].text, root[0][17].text)
    #While the API does have something called away and homescore, it doesn't seem to update or work properly.

class Game:
    def __init__(self, id, sport, time, status, away, home, pregame_odds, live_odds):
        self.id = id
        self.sport = sport
        self.time = time
        self.status = status
        self.away = away
        self.home = home
        self.pregame_odds = pregame_odds
        self.live_odds = live_odds

now = datetime.datetime.now().strftime("%Y-%m-%d")
today_games = scrape_mlb(now)
number_of_games = len(today_games)


html_table = "<table style='width:25%'><tr><th>Home</th><th>Visitor</th><th>Odds</th></tr>"
for i in range(number_of_games):
    html_table += "<tr><td>" + str(today_games[i].home) + "</td>" + "<td>" + str(today_games[i].away) + "</td>" + "<td>" + str(today_games[i].pregame_odds) + "</td></tr>"
html_table += "</table>"

def index(request):
    return HttpResponse(html_table)
