import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

mysql_user = "student"
mysql_password = "Tr!v3raT3ch"
db_url = "mysql+mysqlconnector://%s:%s@localhost/pydemo" % (mysql_user, mysql_password)
# db_url = "sqlite:///:memory: # For SQLite
# print(db_url)

engine = create_engine(db_url, echo=False) # set echo to True for verbose logging
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Knight(Base):
    __tablename__ = 'knights'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    quest = Column(String(255))
    color = Column(String(50))
    comment = Column(String(255))

    def __init__(self, name = "", quest = "", color = "", comment = ""):
        self.name = name
        self.quest = quest
        self.color = color
        self.comment = comment

    def __repr__(self):
        return "<Knight(id=%s, name=%s, quest=%s, color=%s, comment=%s)>" % (self.id, self.name, self.quest, self.color, self.comment)

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
    return Knight(name, quest, color, comment)

def print_knight_table():
    Knight.__table__

def print_knight(knight):
    print(knight)

def create_table():
    Base.metadata.create_all(engine)

def drop_table():
    Knight.__table__.drop(engine)
    session.flush()
    session.commit()

def list_all():
    for knight in session.query(Knight).order_by(Knight.id):
        print(knight)

def add_knight(knight):
    session.add(knight)
    session.flush()
    session.commit()

def quit():
    session.close()
    sys.exit()

def print_menu():
    menu_items=[
            ("Add Knight"),
            ("Add Sir Lancelot"),
            ("Add Sir Robin"),
            ("Add King Arthur"),
            ("List Knights")]
    for idx, menu_item in enumerate(menu_items):
        print("%s) %s" % (str(idx+1), menu_item))
    print("q) Quit")
    # Prompt for a menu item number, default to '5' for 'List Knights' if we get nothing
    mi_num = input("Menu Item # ") or '5'
    # print(mi_num)

    # Instead of a switch-case, we create an anonymous dictionary with lambda functions to invoke and execute based on the input value we just retrieved
    {
            '1': lambda: add_knight(KnightForm()),
            '2': lambda: add_knight(KnightForm(_name = "Sir Lancelot of Camelot", _quest = "To Seek the Holy Grail", _color = "Blue", _comment = "Oh, thank you. Thank you very much.")),
            '3': lambda: add_knight(KnightForm(_name = "Sir Robin of Camelot", _quest = "To Seek the Holy Grail", _color = "I don't know that!", _comment = "Auuuuuuuugh!")),
            '4': lambda: add_knight(KnightForm(_name = "Arthur, King of the Britons", _quest = "To Seek the Holy Grail", _color = "What do you mean? An African or European swallow?", _comment = "Well, you have to know these things when you're a king, you know.")),
            '5': lambda: list_all(),
            'q': lambda: quit()
    }[mi_num]()

# Invoke to interact with existing data and be able to add more:
#   python3 knight_alchemy.py
# Invoke with "drop" to destroy the table (and the data in it):
#   python3 knight_alchemy.py drop
# Invoke with "init" to create the table:
#   python3 knight_alchemy.py init
# Start Fresh; drop and re-create the table (parameter ordering doesn't matter - drop will occur before init):
#   python3 knight_alchemy.py drop init
if __name__ == '__main__':
    if 'drop' in sys.argv:
        drop_table()
    if 'init' in sys.argv:
        create_table()
    while True:
        print_menu()

