import csv
f=open('a.txt','w+')
with open('./training.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    data = [row for row in csv.reader(csvDataFile)]
    for i in range(4040):
        f.write(str(data[i]))
        f.write('\n')
        print(data[i])
