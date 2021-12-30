from flask import Flask
from flask import render_template
from flask import request
import json

app = Flask("Hello World")

@app.route("/")
@app.route("/hello")
def hello():

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

    s = open("spielerdaten.json")
    spielerdaten_list = json.load(s)
    spieler1 = ()
    spieler2 = ()
    spielerindex = 0

    for spieler in spielerdaten_list:
        spieler2 = ((spielerdaten_list[spielerindex]["name"], spielerdaten_list[spielerindex]["team"], spielerdaten_list[spielerindex]["spiele"], spielerdaten_list[spielerindex]["goals"], spielerdaten_list[spielerindex]["assists"],spielerdaten_list[spielerindex]["punkte"]), )
        spieler1 = spieler1 + spieler2
        spielerindex = spielerindex + 1

    spieler1 = sorted(spieler1, key=lambda x: x[5], reverse=True)

    return render_template('index.html', name="Andri", teamliste=team1, spielerliste=spieler1)

@app.route("/test", methods= ["GET", "POST"])
def test():

    if request.method == "POST":
        s = open("spielerdaten.json")
        spielerdaten_list = json.load(s)
        name = request.form["name"]
        team = request.form["team"]
        spiele = request.form["spiele"]
        goals = request.form["goals"]
        assists = request.form["assists"]
        punkte = request.form["punkte"]


        spielerdaten_list.append({"name": name, "team": team, "spiele": spiele, "goals": goals, "assists": assists,"punkte": punkte})

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


