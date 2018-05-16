'''
All the comments indicate what are the things we should take care
to design a function with handling error
'''
def data_cost(filename,*,errortype="warn"):#give the user flexibility to print errors handled so pass a flag but its optional.
                                           # * indicates user must use keyword/named style parameter passing.
                                           # data_cost('Cost.csv',"silent") wont work,('Cost.csv',errortype="silent") will work
    '''
    computes total cost
    :param filename:
    :return:
    '''
    #check the value provided by user is not random values
    if errortype not in ('warn','silent','raise'):
        raise ValueError('errortype must be of "warn","silent","raise"')
    import csv
    total = 0;
    #dont catch error of filenot found here bcoz other functionality which calls this function will catch this
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)  # skip the header row
        for rowno,row in enumerate(rows,start=1):#if we want counters inside for loop this is the best way,pass counter with enumerate
            try:
                row[2] = int(row[2])  # but typecasting we have to do manually
                row[3] = float(row[3])
            except ValueError as err:#Exception as err is generalized version,it catches all error
                #  but dont use it unless u dont know what can be the error,try to narrow down the exception
                # suppose u did syntax mistake inside try block like row[3]=flot(row[3]) it will catch that error too by using Exception
                #show the error msg if user want to
                if errortype == "warn":
                    print('row number',rowno,'Bad row',row)
                    print('reason',err)
                continue #it skips the current row and continues to next row of loop
            except IndexError as err:
                if errortype == "warn":
                    print('row number', rowno, 'Bad row', row)
                    print('reason', err)
                continue  # it skips the current row and continues to next row of loop
            total += row[2] * row[3]
    return total
print(data_cost('Cost1.csv',errortype="warn"))