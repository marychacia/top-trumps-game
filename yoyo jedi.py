from flask import *
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def request_page():
    data_set = [{'Name': 'Darth Maul', 'Honour': 20, 'Anger': 40, 'Greed': 85, 'Battle Skills': 65},
                {'Name': 'Luke Skywalker', 'Honour': 35, 'Anger': 12, 'Greed': 40, 'Battle Skills': 90},
                {'Name': 'Princess Leia', 'Honour': 39, 'Anger': 7, 'Greed': 80, 'Battle Skills': 40},
                {'Name': 'Han Solo', 'Honour': 33, 'Anger': 15, 'Greed': 100, 'Battle Skills': 50},
                {'Name': 'Chewbacca', 'Honour': 18, 'Anger': 5, 'Greed': 125, 'Battle Skills': 55},
                {'Name': 'Darth Vader', 'Honour': 13, 'Anger': 35, 'Greed': 130, 'Battle Skills': 86},
                {'Name': 'Jaba the Hutt', 'Honour': 5, 'Anger': 18, 'Greed': 105, 'Battle Skills': 6},
                {'Name': 'Yoda', 'Honour': 55, 'Anger': 1, 'Greed': 0, 'Battle Skills': 92},
                {'Name': 'Obi-Wan Kenobi', 'Honour': 50, 'Anger': 4, 'Greed': 2, 'Battle Skills': 80},
                {'Name': 'R2-D2', 'Honour': 36, 'Anger': 1, 'Greed': 0, 'Battle Skills': 22},
                {'Name': 'C-3P0', 'Honour': 37, 'Anger': 6, 'Greed': 5, 'Battle Skills': 8},
                {'Name': 'Padme Amidala', 'Honour': 38, 'Anger': 1, 'Greed': 2, 'Battle Skills': 30},
                {'Name': 'Stormtrooper', 'Honour': 15, 'Anger': 24, 'Greed': 50, 'Battle Skills': 12},
                {'Name': 'Bib Fortuna', 'Honour': 7, 'Anger': 14, 'Greed': 55, 'Battle Skills': 32},
                {'Name': 'General Grevious', 'Honour': 2, 'Anger': 12, 'Greed': 117, 'Battle Skills': 70},
                {'Name': 'Greedo', 'Honour': 8, 'Anger': 4, 'Greed' : 5, 'Battle Skills': 28},
                {'Name': 'Lando Calrissian', 'Honour': 13, 'Anger': 4, 'Greed': 75, 'Battle Skills': 49},
                {'Name': 'Jawa', 'Honour': 6, 'Anger': 9, 'Greed': 885, 'Battle Skills': 12},
                {'Name': 'Palpatine', 'Honour': 75, 'Anger': 40, 'Greed': 85, 'Battle Skills': 90},
                {'Name': 'Aayla Secura', 'Honour': 8, 'Anger': 11, 'Greed': 24, 'Battle Skills': 68},
                {'Name': 'Count Dooku', 'Honour': 4, 'Anger': 34, 'Greed': 122, 'Battle Skills': 78},
                {'Name': 'Commander Cody', 'Honour': 30, 'Anger': 6, 'Greed': 20, 'Battle Skills': 39},
                {'Name': 'Jar Jar Binks', 'Honour': 15, 'Anger': 14, 'Greed': 13, 'Battle Skills': 28},
                {'Name': 'Qui-Gon Jinn', 'Honour': 55, 'Anger': 3, 'Greed': 5, 'Battle Skills': 85},
                {'Name': 'Super Battle Droid', 'Honour': 11, 'Anger': 8, 'Greed': 2, 'Battle Skills': 38},
                {'Name': 'Rey', 'Honour': 40, 'Anger': 18, 'Greed': 0, 'Battle Skills': 82},
                {'Name': 'Kylo Ren', 'Honour': 5, 'Anger': 55, 'Greed': 75, 'Battle Skills': 83},
                {'Name': 'Lor San Tekka', 'Honour': 48, 'Anger': 3, 'Greed': 0, 'Battle Skills': 44},
                {'Name': 'Poe Dameron', 'Honour': 38, 'Anger': 6, 'Greed': 4, 'Battle Skills': 63},
                {'Name': 'Finn', 'Honour': 35, 'Anger': 12, 'Greed': 1, 'Battle Skills': 66},
                {'Name': 'Captain Phasma', 'Honour': 33, 'Anger': 19, 'Greed': 84, 'Battle Skills': 55},
                {'Name': 'BB-8', 'Honour': 40, 'Anger': 2, 'Greed': 0, 'Battle Skills': 9},
                {'Name': 'General Hux', 'Honour': 26, 'Anger': 33, 'Greed': 99, 'Battle Skills': 44},
                {'Name': 'Supreme Leader Snoke', 'Honour': 5, 'Anger': 23, 'Greed': 150, 'Battle Skills': 3}
                ]
    jason_dump = json.dumps(data_set)

    return jason_dump

if __name__ == '__main__':
    app.debug = True
    app.run(port=5110)





