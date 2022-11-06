from sqlConnect import *
import readData
from time import sleep


def updateFilm():
    idField = input("Enter the ID of the film to update: ")
    readData.getFilm(idField)
    fieldName = input(
        "Enter the field you want to update (Title, Year, Rating, Duration, Genre): ").title()

    FieldValue = input(f"Enter the new field value for {fieldName}: ")

    cursor.execute(
        f"UPDATE tblFilms SET {fieldName} = '{FieldValue}' WHERE filmID = {idField}")
    conn.commit()
    print(f"Record {idField} updated in songs table")
    sleep(3)
    readData.readFilms()  # invoke the subroutine readSongs from read.py
    
