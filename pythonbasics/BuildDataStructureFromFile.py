
def read_cost(filename,*,errortype="warn"):
    '''
    reads the data of cost and stores in data structure
    :param filename:
    :return:
    '''
    if errortype not in ('warn','silent','raise'):
        raise ValueError('errortype must be of "warn","silent","raise"')
    import csv
    portfolio=[] #list of rows
    total = 0;
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno,row in enumerate(rows,start=1):
            try:
                row[2] = int(row[2])  # but typecasting we have to do manually
                row[3] = float(row[3])
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
            #record =tuple(row),but storing in tuple wont be that much beneficial as we have to pass hardcoded value
            #to extract data.ex-for name,city,houseno,salary in portfolio
            record={'name':row[0],'city':row[1],'business':row[2],'salary':row[3]}
            portfolio.append(record)
    return portfolio