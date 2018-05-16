#tuples
t=("nanda",23,5,67,125.6)#like a row of records,we are doing packing here
t[0]#access like list
a=t[1]*t[2]#Data manipulation
print(a,t[0])
name,age,test1,test2,test3=t#unpacking
#if we will assign like name,age,test1,test2,test3,test4=t,with one extra value it will raise error
#not enough values to unpack (expected 6, got 5)
#tuples are immutable,we cant assign value to tuple like t[0]="testname"
print(name)

#list
#contains same type element
names=['test1','test2','test3','test4']
len(names)
names.append('test5')
names.insert(0,'test0')
#need to see how this two piece code is working
namesconfusion=['test1','test2','test3','test4',5]
namesconfusion[4]*2

#sets
#datatype which removes duplicate from collection

namesset={'test1','test2','test1','test3','test4','test1','test4','test1','test3','test1'}
namesset #{'test1', 'test2', 'test3', 'test4'} removes duplicate
'test4' in namesset#check if test4 is present in sets using in operator,returns true in this case
'test6' in namesset#false
namessetconfused={'test1','test2','test1','test3',2}


#Dictionary

prices={'test1':234,'test2':45,'test3':47}#like javascript dictionary
prices['test1']#key cant be duplicate,can use in operator like sets

#nested dictionary
prices1={'price':{'test1':234,'test2':45,'test3':47},'test2':45,'test3':47}
prices1['price']['test1']#access nested dictionary

