import csv

def read():
    with open('gender.csv', newline='',encoding='Latin-1') as csvFile:
        readCSV = csv.reader(csvFile,delimiter = ',')
        count = 0
        cond = False
        for row in readCSV:
            if not cond:
                header = row
                cond = True
            count = count + 1
            print(row)
            print(row[4],row[8])
        print("count: " , count)
        print(header)