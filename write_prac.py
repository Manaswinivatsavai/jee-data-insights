import csv 
import os
def revenue_Count(price,quantity):
    return price*quantity
files=os.listdir()
for file in files:
    if file.endswith('.csv'):
        with open(file,'r') as rp:
            csvr=csv.reader(rp)
            total=0
            next(csvr)
            print("*"*50)
            print("\t\t{}".format(file))
            print("*"*50)
            for cs in csvr:
                
                price=int(cs[1])
                quantity=int(cs[2])
                revenue=revenue_Count(price,quantity)
                total+=revenue
                print('Revenue: {}'.format(revenue))
        print("Total Revenue:{}".format(total))
        