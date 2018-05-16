def add(x,y):
    '''
    Documentation about add method,type help(add) in cosole to see this msg
    :param x: int
    :param y: int
    :return: addition of two no
    '''
    return x+y
print(add(4,6))
print(add(y=5,x=4))#named arguments no need to worry about order
print(add(y=5,x=4))
add(5,y=6)#ok but order needed,add(4,x=7)#error bcoz we are giving x value to times
help(add)


def data_cost(filename):
    import csv
    total = 0;
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)  # skip the header row
        for rowno,row in enumerate(rows,start=1):#if we want counters inside for loop this is the best way,pass counter with enumerate
            try:
                row[2] = int(row[2])  # but typecasting we have to do manually
                row[3] = float(row[3])
            except ValueError as err:
                print('row number',rowno,'Bad row',row)
                print('reason',err)
                continue #it skips the current row and continues to next row of loop
            total += row[2] * row[3]
    return total
