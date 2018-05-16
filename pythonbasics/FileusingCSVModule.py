'''
from last file we know how to open file and extract data from file,we can read line by line
and then split the data according to comma separator
what if a data value contains comma itself like name can be nanda,nanda
then this will be treated as different values while its a single value.Like this many case we have
handle if we are extracting data manually.
But with the help of CSV module we no need to worry about this
'''
import csv
total=0;
with open('Data.csv','r') as f:
    rows=csv.reader(f)
    headers=next(rows)#skip the header row
    for row in rows:
        row[2]=int(row[2])#but typecasting we have to do manually
        row[3]=float(row[3])
        total +=row[2]*row[3]
print(total)
