#Finding Day of the week
from datetime import date

#accepts two dates month and year from input
# Separate date by slash (/)
d1, m1, y1 = [int(x) for x in input("Enter first date:").split('/')]
d2, m2, y2 = [int(x) for x in input("Enter second date:").split('/')]

#store them
dt1= date(y1, m1, d1)
dt2= date(y2, m2, d2)

#diff in dates
dt = dt1-dt2
print('Days difference= ', dt)

#diff in weeks
weeks, day = divmod(dt.days, 7)
print("Week difference=", weeks)

#diff in months
months, day = divmod(dt.days, 30)
print("Month difference=", months)



