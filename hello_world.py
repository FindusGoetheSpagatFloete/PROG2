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
    teamliste = []

    for team in teamdaten_list:
        max_punkte = int(team["gespielte_spiele"])*3
        punkteausbeute = int(team["punkte_gemacht"])*100/max_punkte
        punkteausbeute = str(round(punkteausbeute,2))
        punkte_pro_spiel = int(team["punkte_gemacht"])/int(team["gespielte_spiele"])
        punkte_pro_spiel = str(round(punkte_pro_spiel,1))
        teamliste.append((team["team_name"], team["gespielte_spiele"], team["tore_geschossen"], team["tore_erhalten"], team["punkte_gemacht"],punkte_pro_spiel, punkteausbeute), )

    teamliste = sorted(teamliste, key=lambda x: x[4], reverse=True)

    s = open("spielerdaten.json")
    spielerdaten_list = json.load(s)
    spielerliste = []

    for spieler in spielerdaten_list:
        punkte_p_spiel = int(spieler["punkte"])/int(spieler["spiele"])
        punkte_p_spiel = str(round(punkte_p_spiel,1))
        spielerliste.append((spieler["name"], spieler["team"], spieler["spiele"], spieler["goals"], spieler["assists"],spieler["punkte"],punkte_p_spiel), )


    spielerliste = sorted(spielerliste, key=lambda x: x[5], reverse=True)





    return render_template('index.html', teamliste=teamliste, spielerliste=spielerliste)

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


