from BuildDataStructureFromFile import read_cost
portfolio=read_cost('Cost.csv',errortype="warn")
#lambda expression similar to others x=>x=x.business
#but here x=lambda x:x.business
portfolio.sort(key= lambda cost:cost['business'])
#reverse sort
portfolio.sort(key= lambda cost:cost['business'],reverse=True)
print(portfolio)

#min,max function
print(min(portfolio,key=lambda cost:cost['salary']))

#group by
import itertools
for field_grouped_by,items in itertools.groupby(portfolio,key= lambda cost:cost['name']):#so here field is 'name' to group
    print(field_grouped_by)
    print('------')
    for item in items:
        print(item)
#we can store into dict using groupby
grouped_by_dict= {'name':list(items) for field_grouped_by,items in itertools.groupby(portfolio,key= lambda cost:cost['name'])}
print(grouped_by_dict)