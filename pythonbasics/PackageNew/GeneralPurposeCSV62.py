#In this type of implementation the problem is we are hardcoding the type casting each time for different values
#we can modify it
def read_CSV(filename,types,*,errortype="warn"):
    '''
    reads the CSV with type conversion
    :param filename:
    :return:
    '''
    if errortype not in ('warn','silent','raise'):
        raise ValueError('errortype must be of "warn","silent","raise"')
    import csv
    records=[] #list of rows
    total = 0;
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno,row in enumerate(rows,start=1):
            try:
                #we are making typecasting using types list and row value
                row=[func(val) for func,val in zip(types,row)]
            except ValueError as err:
                if errortype == "warn":
                    print('row number',rowno,'Bad row',row)
                    print('reason',err)
                continue
            except IndexError as err:
                if errortype == "warn":
                    print('row number', rowno, 'Bad row', row)
                    print('reason', err)
                continue
            record=dict(zip(headers,row))
            records.append(record)
    return records