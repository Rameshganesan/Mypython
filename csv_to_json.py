import csv
import json

csvfile = open('C:\Users\Ganesr01\Desktop\ifrs_test.csv', 'r')
jsonfile = open('C:\Users\Ganesr01\Desktop\ifrs_test.json', 'w')

fieldnames = ("P","cnt","trCurr","amntTC","amntRC","posId","mastId","univAcc","amntNat","pma")
reader = csv.DictReader(csvfile, fieldnames)
print(reader)
for row in reader:
    print(row)
    #json.dump(row, jsonfile)
    #jsonfile.write('\\n')