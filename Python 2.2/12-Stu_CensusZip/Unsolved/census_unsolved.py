# import modules

import os
import csv

# open the census starter file
censusCSV = os.path.join(".", "Resources", "census_starter.csv")

print(censusCSV)


# create lists to store the data from the original csv file
places = []
populations = []
incomes = []
poverty_counts = []

# read the original csv file and grab the necessary data ( populate the lists)
with open(censusCSV, "r", encoding="utf-8") as file: 

    #create the reader object (file stream)
    csvreader = csv.reader(file, delimiter= ",")

# read each row of data from the file
for row in csvreader:
    # grab the place and append to the places list
    places.append(row[0])

    # grab the population (row[1]) and append to the populations list
    populations.append(row[1])

    # grab the income (row[4]) for each row and append to the incomes list
    incomes.append(row[4])

    # grab the poverty count (row[8])
    poverty_counts.append(row[8])


# zip all of the data together into tuples
cleanedData = zip(places, populations, incomes, poverty_counts)

# extract that zipped data into an output file
outputLocation = os.path.join("censusCleaned.csv") # creates a file in the same folder as the python file since not specifiying any additiaonl arugments

# open the output file and write the zipped data to it
with open(outputLocation, "w", newline="") as outFile:
    # set up the writer
    csvwriter = csv.writer(outFile)

    # write a header row
    csvwriter.writerow(["Place", "Population", "Per Capita Income", "PovertyCount"])
    


