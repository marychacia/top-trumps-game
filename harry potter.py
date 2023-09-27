from flask import *
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def request_page():
    data_set = [{'Name': 'Harry Potter', 'House': 'Griffindor', 'Magic': 75, 'Cunning': 40, 'Wisdom': 85, 'Courage': 90},
                {'Name': 'Hermione Granger', 'House': 'Griffindor', 'Magic': 85, 'Cunning': 30, 'Wisdom': 100, 'Courage': 70},
                {'Name': 'Ron Weasley', 'House': 'Griffindor', 'Magic': 45, 'Cunning': 15, 'Wisdom': 30, 'Courage': 65},
                {'Name': 'Luna Lovegood', 'House': 'Ravenclaw', 'Magic': 44, 'Cunning': 14, 'Wisdom': 70, 'Courage': 65},
                {'Name': 'Draco Malfoy', 'House': 'Slytherin', 'Magic': 60, 'Cunning': 55, 'Wisdom': 50, 'Courage': 25},
                {'Name': 'Rubeus Hagrid', 'House': 'Griffindor', 'Magic': 20, 'Cunning': 13, 'Wisdom': 20, 'Courage': 45},
                {'Name': 'Severus Snape', 'House': 'Slytherin', 'Magic': 120, 'Cunning': 100, 'Wisdom': 110, 'Courage': 100},
                {'Name': 'Feurir Greyback', 'House': 'Slytherin', 'Magic': 55, 'Cunning': 40, 'Wisdom': 40, 'Courage': 9},
                {'Name': 'Bellatrix Lestrange', 'House': 'Slytherin', 'Magic': 112, 'Cunning': 55, 'Wisdom': 60, 'Courage': 10},
                {'Name': 'Lord Voldemort', 'House': 'Slytherin', 'Magic': 120, 'Cunning': 42, 'Wisdom': 90, 'Courage': 0},
                {'Name': 'Mr Olivander', 'House': 'Ravenclaw', 'Magic': 68, 'Cunning': 20, 'Wisdom': 72, 'Courage': 40},
                {'Name': 'Minerva Mcgonagall', 'House': 'Griffindor', 'Magic': 95, 'Cunning': 29, 'Wisdom': 80, 'Courage': 75},
                {'Name': 'Cho Chang', 'House': 'Ravenclaw', 'Magic': 50, 'Cunning': 12, 'Wisdom': 40, 'Courage': 34},
                {'Name': 'Professor Flitwick', 'House': 'Ravenclaw', 'Magic': 85, 'Cunning': 25, 'Wisdom': 105, 'Courage': 75},
                {'Name': 'Rubeus Hagrid', 'House': 'Griffindor', 'Magic': 20, 'Cunning': 13, 'Wisdom': 20, 'Courage': 45},
                {'Name': 'Cedric Diggory', 'House': 'Hufflepuff', 'Magic': 86, 'Cunning': 20, 'Wisdom': 85, 'Courage': 60},
                {'Name': 'Hannah Abbott', 'House': 'Hufflepuff', 'Magic': 50, 'Cunning': 4, 'Wisdom': 45, 'Courage': 10},
                {'Name': 'Helga Hufflepuff', 'House': 'Hufflepuff', 'Magic': 89, 'Cunning': 23, 'Wisdom': 102, 'Courage': 50},
                {'Name': 'Ernie Macmillan', 'House': 'Hufflepuff', 'Magic': 45, 'Cunning': 10, 'Wisdom': 50, 'Courage': 55},
                {'Name': 'Nymphadora Tonks', 'House': 'Hufflepuff', 'Magic': 76, 'Cunning': 18, 'Wisdom': 64, 'Courage': 66},
                {'Name': 'Professor Sprout', 'House': 'Hufflepuff', 'Magic': 48, 'Cunning': 10, 'Wisdom': 70, 'Courage': 54},
                {'Name': 'Rowena Ravenclaw', 'House': 'Ravenclaw', 'Magic': 115, 'Cunning': 60, 'Wisdom': 125, 'Courage': 95},
                {'Name': 'Gilderoy Lockart', 'House': 'Ravenclaw', 'Magic': 15, 'Cunning': 85, 'Wisdom': 8, 'Courage': 0},
                {'Name': 'Quirinus Quirrell', 'House': 'Ravenclaw', 'Magic': 50, 'Cunning': 75, 'Wisdom': 52, 'Courage': 15},
                {'Name': 'Moaning Myrtle', 'House': 'Ravenclaw', 'Magic': 0, 'Cunning': 15, 'Wisdom': 28, 'Courage': 10},
                {'Name': 'Padma Patil', 'House': 'Ravenclaw', 'Magic': 40, 'Cunning': 15, 'Wisdom': 32, 'Courage': 15},
                {'Name': 'Xenophilius Lovegood', 'House': 'Ravenclaw', 'Magic': 50, 'Cunning': 5, 'Wisdom': 37, 'Courage': 23},
                {'Name': 'Sirius Black', 'House': 'Griffindor', 'Magic': 75, 'Cunning': 63, 'Wisdom': 50, 'Courage': 85},
                {'Name': 'Albus Dumbledore', 'House': 'Griffindor', 'Magic': 120, 'Cunning': 15, 'Wisdom': 105, 'Courage': 100},
                {'Name': 'Remus Lupin', 'House': 'Griffindor', 'Magic': 70, 'Cunning': 63, 'Wisdom': 55, 'Courage': 80},
                {'Name': 'Neville Longbottom', 'House': 'Griffindor', 'Magic': 55, 'Cunning': 25, 'Wisdom': 48, 'Courage': 75},
                {'Name': 'The Bloody Baron', 'House': 'Slytherin', 'Magic': 0, 'Cunning': 100, 'Wisdom': 60, 'Courage': 10},
                {'Name': 'Nearly Headless Nick', 'House': 'Griffindor', 'Magic': 0, 'Cunning': 30, 'Wisdom': 47, 'Courage': 39},
                {'Name': 'Peeves', 'House': 'None', 'Magic': 0, 'Cunning': 105, 'Wisdom': 30, 'Courage': 5},
                {'Name': 'Troll', 'House': 'Troll', 'Magic': 0, 'Cunning': 20, 'Wisdom': 0, 'Courage': 3},
                {'Name': 'Firenze', 'House': 'Centaur', 'Magic': 52, 'Cunning': 10, 'Wisdom': 103, 'Courage': 53},
                {'Name': 'Romilda Vane', 'House': 'Griffindor', 'Magic': 43, 'Cunning': 19, 'Wisdom': 23, 'Courage': 21},
                {'Name': 'Ginny Weasley', 'House': 'Griffindor', 'Magic': 83, 'Cunning': 22, 'Wisdom': 48, 'Courage': 58},
                {'Name': 'Dobby', 'House': 'House-elf', 'Magic': 100, 'Cunning': 2, 'Wisdom': 44, 'Courage': 53},
                {'Name': 'Fleur Delacour', 'House': 'None', 'Magic': 70, 'Cunning': 20, 'Wisdom': 57, 'Courage': 33},
                {'Name': 'Dolores Umbridge', 'House': 'None', 'Magic': 36, 'Cunning': 110, 'Wisdom': 30, 'Courage': 6},
                {'Name': 'Molly Weasley', 'House': 'None', 'Magic': 45, 'Cunning': 22, 'Wisdom': 64, 'Courage': 72},
                {'Name': 'P Weasley', 'House': 'None', 'Magic': 0, 'Cunning': 20, 'Wisdom': 0, 'Courage': 3},
                {'Name': 'Peter Pettigrew', 'House': 'None', 'Magic': 16, 'Cunning': 98, 'Wisdom': 15, 'Courage': 4},
                {'Name': 'James Potter', 'House': 'None', 'Magic': 69, 'Cunning': 14, 'Wisdom': 40, 'Courage': 43},
                {'Name': 'Lily Potter', 'House': 'None', 'Magic': 78, 'Cunning': 7, 'Wisdom': 53, 'Courage': 89},
                {'Name': 'Fred Weasley', 'House': 'None', 'Magic': 77, 'Cunning': 13, 'Wisdom': 22, 'Courage': 30},
                {'Name': 'George Weasley', 'House': 'None', 'Magic': 77, 'Cunning': 11, 'Wisdom': 23, 'Courage': 33},
                {'Name': 'Lucious Malfoy', 'House': 'None', 'Magic': 81, 'Cunning': 101, 'Wisdom': 24, 'Courage': 20},
                {'Name': 'Alastor Moody', 'House': 'None', 'Magic': 48, 'Cunning': 30, 'Wisdom': 54, 'Courage': 33},
                {'Name': 'Horace Slughorn', 'House': 'None', 'Magic': 72, 'Cunning': 44, 'Wisdom': 28, 'Courage': 21}]
    jason_dump = json.dumps(data_set)

    return jason_dump

if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)