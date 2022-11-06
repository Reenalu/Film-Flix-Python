from sqlConnect import *
import readData
from time import sleep


def deleteFilm():
    # songID of the record to be deleted
    idField = input("Enter the filmID to be deleted : ")

    cursor.execute(f"DELETE FROM tblFilms WHERE filmID={idField}")
    conn.commit()
    print(f"FilmID {idField} deleted from Film table")  # return the deleted SongID

    sleep(3)
    readData.readData()  # call the readSongs methiod from the readData python file


  # call the deleteSongs



