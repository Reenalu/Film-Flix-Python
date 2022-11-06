from sqlConnect import *


def readFilms():
    cursor.execute("SELECT * FROM tblFilms")
    row = cursor.fetchall()
    for record in row:
        print(record)



