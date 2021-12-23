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
    s = open("teamdaten.json")
    teamdaten_list = json.load(s)
    team1 = ()
    team2 = ()
    teamindex = 0

    for team in teamdaten_list:
        team2 = ((teamdaten_list[teamindex]["team_name"], teamdaten_list[teamindex]["gespielte_spiele"], teamdaten_list[teamindex]["tore_geschossen"], teamdaten_list[teamindex]["tore_erhalten"], teamdaten_list[teamindex]["punkte_gemacht"]), )
        team1 = team1 + team2
        teamindex = teamindex + 1

    team1 = sorted(team1, key=lambda x: x[4], reverse=True)
    return render_template('index.html', name="Andri",ergebnis=zahl, teamliste=team1)

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

@app.route("/team_formular", methods= ["GET", "POST"])
def team_formular():
    if request.method == "POST":
        s = open("teamdaten.json")
        teamdaten_list = json.load(s)
        teamname = request.form["team_name"]
        gespieltespiele = request.form["gespielte_spiele"]
        toregeschossen = request.form["tore_geschossen"]
        toreerhalten = request.form["tore_erhalten"]
        punktegemacht = request.form["punkte_gemacht"]


        teamdaten_list.append({"team_name": teamname, "gespielte_spiele": gespieltespiele, "tore_geschossen": toregeschossen, "tore_erhalten": toreerhalten, "punkte_gemacht": punktegemacht})

        with open("teamdaten.json", "w") as f:
            json.dump(teamdaten_list, f, indent=4, separators=(",", ":"), sort_keys=True)




    return render_template('team_formular.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)


