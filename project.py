# Pool Table Management System

import datetime
import time

class Tables:
    def __init__(self, number):
        self.number = number
        self.start_time = ""
        self.occupancy = "Unoccupied"

tables = []

for index in range(0, 12):
    new_table = Tables(index + 1)
    tables.append(new_table)

def show_time(table):
    start = table.start_time
    end = datetime.datetime.now()
    elapsed = end - start
    return elapsed 

def show_tables():
    for table in tables:
        print(f'Table {table.number} {table.occupancy}')

name = input("Enter name: ")

def pool_table_intro():
    print(f"Hi {name}! Welcome to the Pool Table Management System.") 
    print("")

def cost_of_play(total_time):
    start = table.start_time
    end = datetime.datetime.now()
    total_time = (end - start).total_seconds()
    mins = int(total_time/60)
    rate = 0.5
    cost = rate * mins
    with open("pooltable.txt", "a+") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Table number: {table.number}\n")
        file.write(f"Start: {start}\n")
        file.write(f"End: {end}\n")
        file.write(f"Total time: {mins}\n")
        file.write(f"Cost: {cost}\n")
        file.write("")
    return(f"Total time played: {mins} minutes. The cost is {cost}.")

running = True

while running:
    print("")
    pool_table_intro()
    print("Press 1 to see available tables")
    print("Press 2 to reserve a table")
    print("Press 3 to see time elapsed on occupied tables")
    print("Press 4 to close table")
    print("")
    user_input = input("Please choose an option: ")

    if user_input == "1":
        print("")
        print("Here are the pool tables:")
        print("")
        show_tables()
        
    elif user_input == "2":
        print("")
        table_selection = int(input("Which table would you like? "))
        print("")
        table = tables[table_selection -1]
        if table.occupancy == "Occupied":
            print("*** Table occupied! ***")
            print("")
        else:
            print(f'*** You have reserved table {table.number} ***')
            table.occupancy = "Occupied"
            table.start_time = datetime.datetime.now()

    elif user_input == "3":
        for table in tables:
            if table.occupancy == "Occupied":
                elapsed = show_time(table)
                print("")
                print(f'Patrons on table {table.number} have been there for {elapsed}')
                print("")

    elif user_input == "4":
        print("")
        table_selection = int(input("Which table are you closing? "))
        print("")
        table = tables[table_selection -1]
        if table.occupancy == "Occupied":
            elapsed = show_time(table)
            table.occupancy = "Unoccupied"
            print(f'You have closed table {table.number}.')
            print("")
            total_cost = cost_of_play(elapsed)
            print(total_cost)
            print("")
        else: 
            print("That table is not occupied.")

    elif user_input == "q":
        print("")
        break

    else:
        print("")
        print("Error! Please choose from the menu below or press q to quit.")

