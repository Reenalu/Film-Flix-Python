from sqlConnect import *
from time import sleep

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
            genreName = input(f"Please enter the genre name: ")
            cursor.execute(f"SELECT * FROM tblFilms WHERE genre = \"{genreName.title()}\"")
            row = (cursor.fetchall())
            for record in row:
                print(record)
    elif reportOptions == "3":
            yearInput = input(f"Please enter the Year the Film was Released: ")
            cursor.execute(f"SELECT * FROM tblFilms WHERE yearReleased = \"{yearInput.title()}\"")
            row = (cursor.fetchall())
            for record in row:
                print(record)
    elif reportOptions == "4":
            ratings = input(f"Please enter the Film Rating: ")
            cursor.execute(f"SELECT * FROM tblFilms WHERE rating = \"{ratings.title()}\"")
            row = (cursor.fetchall())
            for record in row:
                 print(record)
    elif reportOptions == "" :
            option = 0
            return reportOptions
    
    if (len(row) == 0):
        print("Please check your spelling and try again.")
        # reportOptions()
    else:
        print(f"{len(row)} records returned")
        for record in row:
            print(record)
            
    sleep(3)





   