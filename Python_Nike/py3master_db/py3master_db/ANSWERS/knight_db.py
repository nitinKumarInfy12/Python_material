#!/usr/bin/env python
# (c)2018 Trivera Tech
# Movie Quotes from "Monty Python and the Holy Grail", Scene 22:
# http://montypython.50webs.com/scripts/Holy_Grail/Scene22.htm
import sys
import os
import sqlite3
import sqlalchemy



DB_NAME = 'DATA/knights.db'

def KnightForm(_name = "", _quest = "", _color = "", _comment = ""):
    print("Stop! Who would cross the Bridge of Death must answer me these questions three, ere the other side he see.")
    name = input("What... is your name? [%s]" % _name) or _name
    quest = input("What... is your quest? [%s]" % _quest) or _quest
    if "Robin" in name:
        color = input("What... is the capital of Assyria? [%s]" % _color) or _color
        comment = input("Comment: [%s] " % _comment) or _comment
    elif "Arthur" in name:
        color = input("What... is the air-speed velocity of an unladen swallow? [%s]" % _color) or _color
        print("Huh? I-- I don't know that. Auuuuuuuugh!")
        comment = input("How do know so much about swallows? [%s]" % _comment) or _comment
    else:
        color = input("What... is your favorite color? [%s]" % _color) or _color
        print("Off you go!")
        comment = input("Comment: [%s] " % _comment) or _comment
    return (name, quest, color, comment)

def create_db():
    os.unlink(DB_NAME)


def update_db(form):
    print("Name:", form.name.data)
    print("Quest:", form.quest.data)
    print("Color:", form.color.data)
    print("Comment:", form.comment.data)
    with sqlite3.connect(DB_NAME) as s3conn:
        pass

def printKnight(knight):
    print()
    print(knight[0])
    print(knight[1])
    print(knight[2])
    print(knight[3])
    print()

if __name__ == '__main__':
    if 'initdb' in sys.argv:
        create_db()
    #
    form = KnightForm(_name = "Sir Lancelot of Camelot", _quest = "To Seek the Holy Grail", _color = "Blue", _comment = "Oh, thank you. Thank you very much.")
    printKnight(form)

    #
    form = KnightForm(_name = "Sir Robin of Camelot", _quest = "To Seek the Holy Grail", _color = "I don't know that!", _comment = "Auuuuuuuugh!")
    printKnight(form)

    # Enter appropriate responses for Sir Galahad:
    form = KnightForm()
    printKnight(form)

    #
    form = KnightForm(_name = "Arthur, King of the Britons", _quest = "To Seek the Holy Grail", _color = "What do you mean? An African or European swallow?", _comment = "Well, you have to know these things when you're a king, you know.")
    printKnight(form)


