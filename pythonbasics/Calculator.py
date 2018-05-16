principal=50000
payment=9265.12
rate=0.05
total_paid=0
while principal>0:
    interest=principal*(rate/12)
    principal=principal+interest-payment
    total_paid+=payment
print(total_paid,interest,principal)
'''
format the output
%10d-means width is 10 to display and its int type,for string %s and for float %f
10.2f means 2 digits allowed after decimal point
'''
name='nanda'
age=24
salary=0.5657
print('%10d %10s %10.2f' % (age,name,salary))
#right aligned due to :> sign,can see it in output
print('{:>10d} {:>10s} {:>10.2f}'.format(age,name,salary))
print('{:<10d} {:<10s} {:<10.2f}'.format(age,name,salary))