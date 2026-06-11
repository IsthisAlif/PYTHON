# Python Writing files (.txt, .json, .csv)

import json
import csv

# txt
employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

file_path1 = "Tutorial/File/Writing Path/output.txt"


try:
    with open(file=file_path1, mode="w") as file:
        for employee in employees:
            file.write(employee + "\n")
        print(f"txt file '{file_path1}' was created")
except FileExistsError:
    print("That file already exists")

# json
employee = {
    "name" : "Spongebob",
    "age" : 30,
    "job" : "cook"
}

file_path2 = "Tutorial/File/Writing Path/output.json"

try:
    with open(file=file_path2, mode="w") as file:
        json.dump(employee, file, indent=4)
        print(f"json file '{file_path2}' is created")
except FileExistsError:
    print("That file already exists")

# csv
employees = [["Name", "Age", "Job"],
             ["Spongebob", 30, "Cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"]]

file_path3 = "Tutorial/File/Writing Path/output.csv"

try:
    with open(file=file_path3, mode="w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path3}' is created")
except FileExistsError:
    print("That file already exists")