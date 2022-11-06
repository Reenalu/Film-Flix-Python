from sqlConnect import *
from readData import *
from time import sleep


def addFilm():
    film = []

    Name = input("Please input the film name: ")
    yearReleased = int(input("Please input the film year released: "))
    Rating = input("Please input the film age rating: ")
    Duration = int(input("Please input the film duration(in minutes): "))
    Genre = input("Please input the film genre: ")

    film.append(Name)
    film.append(yearReleased)
    film.append(Rating)
    film.append(Duration)
    film.append(Genre)

    cursor.execute(
        f"INSERT INTO tblFilms VALUES(null, ?, ?, ?, ?, ?)", film)

    conn.commit()
    print(f"{Name} added to the songs table")
    sleep(3)
    
