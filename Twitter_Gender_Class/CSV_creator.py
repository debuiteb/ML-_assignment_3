import csv

def read():
    with open('gender.csv', newline='',encoding='Latin-1') as csvFile:
        readCSV = csv.reader(csvFile,delimiter = ',')
        count = 0
        cond = False

        data = list()

        newCSV = open('cleaned_gender.csv' , 'w', newline='',encoding='Latin-1' )
        with newCSV:
            writer = csv.writer(newCSV)
            for row in readCSV:
                if not cond:
                    header = row
                    cond = True
                    data.append(header)
                count = count + 1
                #print(row)
                if row[5] == 'male' or row[5] == 'female' or row[5] == 'brand':
                    #add to data
                    data.append(row)
                    #print("g:",row[5])
            writer.writerows(data)
        #print("count: " , count)
        #print(header)
    return ".//cleaned_gender.csv"