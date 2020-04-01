import csv
SizeList=[]
ResistanceList=[]
myList=[]
def LoadCSV():
    with open('resistanceLookup.csv',mode='r', newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=' ')
        myList = list(reader)
        for i  in range(1,len(myList)):
            SizeList.append(myList[i][0].partition(',')[0])
            ResistanceList.append(myList[i][0].partition(',')[2])

def GivenSizeFindResistance(size):
    toReturn=-1
    for index in SizeList:
        if(size == index):
            toReturn = ResistanceList[index]
    return toReturn

#TODO: Size lookup table
