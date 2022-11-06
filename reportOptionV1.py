from sqlConnect import *
from time import sleep
import datetime

curDateTime = datetime.datetime.now()
curYear = curDateTime.year

def reportOptions():
    reportOptions = 0
    while reportOptions not in ["1", "2", "3", "4", "5", ""]:
        print("Film Menu options \nEnter \n1. Print details of all films \n2. Print all films of a particular genre \n3. Print all films of a particular year \n4. Print all films of a particular rating\n5. Exit to Main Menu")

        reportOptions = input(
            "Enter one of the options listed above (Press Enter to exit): ")

    if reportOptions not in ["1", "2", "3", "4", ""]:
            print("Please enter one of the options")
        
    if reportOptions == "1":
            cursor.execute(f"SELECT * FROM tblFilms")
            row = (cursor.fetchall())
            for record in row:
                 print(record)
    elif reportOptions == "2":
            genreName = input(f"Please enter the genre name: ").title()
            genreList = ["Action", "Crime", "Animation", "Adventure", "Comedy", "Horror"]
            if genreName in genreList:
                cursor.execute(f"SELECT * FROM tblFilms WHERE genre = \"{genreName}\"")
                row = (cursor.fetchall())
                for record in row:
                    print(record)
            else:
                print(f"The Genre {genreName} is not valid")        
    elif reportOptions == "3":
            yearInput = input(f"Please enter the Year the Film was Released: ")
            if yearInput <= str(curYear): #datetime.datetime.now(%G):
                cursor.execute(f"SELECT * FROM tblFilms WHERE yearReleased = \"{yearInput}\"")
                row = (cursor.fetchall())
                for record in row:
                    print(record)
            else:
                print(f"The date {yearInput} is greater than 2022")
    elif reportOptions == "4":
            ratings = input(f"Please enter the Film Rating: ").title()
            ratingList = ["G", "PG", "12", "15", "18", "R"]
            if ratings in ratingList:
                cursor.execute(f"SELECT * FROM tblFilms WHERE rating = \"{ratings}\"")
                row = (cursor.fetchall())
                for record in row:
                    print(record)
            else:
                print(f"The Rating {ratings} is not valid")
    elif reportOptions == "" :
            option = 0
            return reportOptions
            
    sleep(3)





   