from flask import Flask
from flask import render_template
from flask import request
import json

app = Flask("Hello World")

@app.route("/")
@app.route("/hello")
def hello():
    bla = 23 / 12
    zahl = round(bla, 2)
    return render_template('index.html', name="Andri",ergebnis=zahl)

@app.route("/test", methods= ["GET", "POST"])
def test():

    if request.method == "POST":
        s = open("spielerdaten.json")
        spielerdaten_list = json.load(s)
        vorname = request.form["vorname"]
        nachname = request.form["nachname"]
        team = request.form["team"]
        goals = request.form["goals"]
        assists = request.form["assists"]
        punkte = request.form["punkte"]


        spielerdaten_list.append({"vorname": vorname, "nachname": nachname, "team": team, "goals": goals, "assists": assists,"punkte": punkte})

        with open("spielerdaten.json", "w") as f:
            json.dump(spielerdaten_list, f, indent=4, separators=(",", ":"), sort_keys=True)


    return render_template('spieler_formular.html')

@app.route("/team_formular")
def team_formular():
    return render_template('team_formular.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)


