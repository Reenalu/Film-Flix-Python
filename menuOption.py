import readData, insertData, updateData, deleteData, reportOptionV1

def menuOptions():
    options = 0
    while options not in ["1", "2", "3", "4", "5", ""]:
        print("Film Menu options \nEnter \n1. Print a Film Name \n2. Add a Film \n3. Update a Film.\n4. Delete a Film.\n5. Read Film Report")

        options = input(
            "Enter one of the options listed above (Press Enter to exit): ")

        if options not in ["1", "2", "3", "4", "5", ""]:
            print("please enter one of the options")

        return options


mainProgram = True
mainMenu = 0
while mainProgram:
    mainMenu = menuOptions()

    if mainMenu == "1":
        readData.readFilms()
    elif mainMenu == "2":
        insertData.addFilm()
    elif mainMenu == "3":
        updateData.updateFilm()
    elif mainMenu == "4":
        deleteData.deleteFilm()
    elif mainMenu == "5":
        reportOptionV1.reportOptions()
    elif mainMenu == "":
        mainProgram = False
    else:
        print("An Error Occured")