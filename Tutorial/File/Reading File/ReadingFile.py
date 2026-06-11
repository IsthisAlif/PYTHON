# Python Reading File (.txt, .json, .csv)

import json
import csv

# txt
file_path1 = "Tutorial/File/Reading File/input.txt"
try:
    with open(file_path1, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")

# json
file_path2 = "Tutorial/File/Reading File/input.json"
try:
    with open(file_path2, "r") as file:
        content = json.load(file)
        print(content["job"])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")

# csv
file_path3 = "Tutorial/File/Reading File/input.csv"
try:
    with open(file_path3, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line[0])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")