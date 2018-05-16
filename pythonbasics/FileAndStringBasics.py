'''
different ways to open file
'''
#1st read whole
f=open('Data.csv','r')
data=f.read()
print(data)
f.close()

#2nd read line by line
f1=open('Data.csv','r')
for line in f1:
    print(line)
f1.close()

#3rd with is like using in other namguase,so no need to write explicit close for this
with open('Data.csv','r') as f2:
    data=f2.read()

#string basics

a="hello world"
b='with ,"single", quote\n'
a[0]#we can access characters using index
a[-1]#start from last index towards 0th index
a[-5]
a[2:4]#gives range of character
a[-5:]#gives last five letter
a[:5]#gives first five letter
len(a)#gives length
c=a+b#concatenate a and b
b.strip()#clean white spaces at start or end,here it will clean /n
b.strip('"')#clean double quotes
b.replace('w','h')
k=b.split(',')#it creates a list now b[0] will give the first part of string
