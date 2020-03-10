import csv
SizeList=[]
ResistanceList=[]
def LoadCSV():
    with open('resistanceLookup.csv',mode='r', newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=' ')
        myList = list(reader)
        print()

        for row in reader:
            SizeList.append(myList[0][0].partition(',')[0])
            ResistanceList.append(myList[0][0].partition(',')[2])