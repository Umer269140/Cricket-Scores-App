from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import re
import random

app = Flask(__name__)

TEAM_TO_COUNTRY = {
    "India": "in",
    "Australia": "au",
    "England": "gb",
    "South Africa": "za",
    "New Zealand": "nz",
    "Pakistan": "pk",
    "Sri Lanka": "lk",
    "West Indies": "bb",
    "Bangladesh": "bd",
    "Afghanistan": "af",
    "Ireland": "ie",
    "Zimbabwe": "zw",
    "Netherlands": "nl",
    "Scotland": "gb",
    "United Arab Emirates": "ae",
    "Nepal": "np",
    "Oman": "om",
    "Papua New Guinea": "pg",
    "United States": "us",
    "Namibia": "na",
    "Canada": "ca",
    "Hong Kong": "hk",
    "Kenya": "ke",
    "Bermuda": "bm",
    "East Africa": "eac",
}

def get_team_info(team_name):
    for team, code in TEAM_TO_COUNTRY.items():
        if team in team_name:
            return {"name": team, "flag": code}
    return None

@app.route('/')
def index():
    try:
        response = requests.get('https://static.cricinfo.com/rss/livescores.xml')
        soup = BeautifulSoup(response.content, 'xml')
        items = soup.find_all('item')
        scores = []
        for item in items:
            title = item.title.text
            teams_in_title = re.split(r'\s+vs\s+', title, maxsplit=1)
            
            teams_data = []
            if len(teams_in_title) == 2:
                team1_info = get_team_info(teams_in_title[0])
                team2_info = get_team_info(teams_in_title[1])
                if team1_info:
                    teams_data.append(team1_info)
                if team2_info:
                    teams_data.append(team2_info)

            prediction = ""
            if len(teams_data) == 2:
                winner = random.choice([teams_data[0]['name'], teams_data[1]['name']])
                prediction = f"{winner} has a 60% chance of winning."

            scores.append({'title': title, 'teams': teams_data, 'prediction': prediction})
        return render_template('index.html', scores=scores)
    except requests.exceptions.RequestException as e:
        return f"Error fetching data: {e}"

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)