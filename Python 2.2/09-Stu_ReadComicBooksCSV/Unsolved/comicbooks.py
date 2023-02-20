#import modules
import os # allows to handle file paths
import csv # allows to handle csv files

# ask the user for the title
title = input("What title are you searching for? ")

# set the file path for the csv file
# currently we are in unsolver foler, so have to go up 2 folders to get to resources, then choose the comic_books.csv file

csvpath = os.path.join("..", "Resources", "comic_books.csv") # .. goes up 2 folders

# print the path
# print(csvpath)

# search through the file

# first, open the file for reading
with open(csvpath, 'r', encoding="utf-8") as file: #utf-8 is unicode text format 8 bit which holds vast majoirty of alphanumeric characters as well as accent markers
    # 'r' is for read mode

    # create the reader object
    csvreader = csv.read(file, delimiter=",")

    csvheader = next(csvreader)

    # set a variable to check to see if the comic title was found
    found = False

    # looping through the remaining rows to search for the title
    for row in csvreader:
        # check for the matching title in the title column ([0])
        if row[0] == title:
            # print the title, publisher (row[8]), and year (row[9])
            print(f"{row[0]} was publishe dby {row[8]} in {row[9]}")
            # if the title is found, set the flag to true
            found = True


    # if the title is never found, print a message infomring the user
    if found == False:
        print(f"{title} was not ofund in this dataset")