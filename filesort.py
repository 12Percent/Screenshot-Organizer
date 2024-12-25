import os
import shutil

dates = {
    'january':'01',
    'february':'02',
    'march':'03',
    'april':'04',
    'may':'05',
    'june':'06',
    'july':'07',
    'august':'08',
    'september':'09',
    'october':'10',
    'november':'11',
    'december':'12'
}

keepGoing = True

inputPath = input("Enter path: ")
path = r"" + inputPath

# testing if path is found
# print(os.listdir(path))       

# make a list containing all files
fileName = os.listdir(path)

keepGoing = input("Sort files (y/n)? ")

while keepGoing == 'y':
    
    month = input("Enter month: ").lower()
    year = input("Enter year: ")
    nextFolder = year + "-" + dates[month]
    
    # check if folder exists. if not, create folder with certain format (i.e. december 2024)
    if os.path.exists(path + "/" + month + " " + year):
        print("\nFolder already exists.")
    else: 
        os.makedirs(path + "/" + month + " " + year)
        
    # traverse through the list and move files if a matching month/year is found in each file's name
    for file in fileName:
        if nextFolder in file and not os.path.exists(path + month + " " + year + "/" + file):
             shutil.move(path + "/" + file, path + "/" + month + " " + year + "/" + file)

    print("Files sorted.\n")
    keepGoing = input("Continue sorting? (y/n) ")