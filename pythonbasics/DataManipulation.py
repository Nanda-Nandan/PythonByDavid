from BuildDataStructureFromFile import read_cost
portfolio=read_cost('Cost.csv',errortype="warn")
#list comprehension
#2nd part is like for loop ,adding the evaluation expression in front of loop to build a list comprehension
#costs['business']+costs['salary'] for costs in portfolio statement creating a list for each row
totalcost=sum(costs['business']+costs['salary'] for costs in portfolio)
#its like linq query,most end with ']' to store in variable because python will know
#we are storing in list variables
morebusiness=[costs['name'] for costs in portfolio if costs['business']>160]
#set comprehension,storing into set by adding } at end
morebusinessset={costs['name'] for costs in portfolio if costs['business']>100}
#morebusinesstouple=(costs['name'] for costs in portfolio if costs['business']>100) is wrong,no tuple comprehension
businesscategory=['hotel','shop','grocery','milk','water','farm','fish']
#zip function
#takes two sequence of data,pairs it
#if the size unmatches it pairs to smallest size
for category,cost in zip(businesscategory,morebusinessset):
    print(category,'---',cost)
    #if size unmatches create dictionary of length of smaller one
dictpairs= dict(zip(businesscategory,morebusinessset))
print(dictpairs)
#Dictionary comprehension
dictcomprehensionvalue={category:cost for category,cost in zip(businesscategory,morebusinessset)}
print(totalcost,morebusiness,morebusinessset,dictcomprehensionvalue)