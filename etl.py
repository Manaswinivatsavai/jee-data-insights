import csv 
def revenue(price,quantity):
    return price*quantity
def extract(filename):
    data=[]
    try:
        with open (filename,'r') as rp:
                read=csv.reader(rp)
                next(read)
                for r in read:
                    data.append(r)
        return data
    except FileNotFoundError:
        print("File not found")
    
def transform(data):
    processes=[]
    for d in data:
        try:
            order=d[0]
            price=int(d[1])
            quantity=int(d[2])
            
        except ValueError:
            print("Skipping Invalid Data {}".format(d))
        else:
            rev=revenue(price,quantity)
            processes.append([order,price,quantity,rev])
    return processes

def load(data):
    with open ('example.csv','w') as wp:
        write=csv.writer(wp)
        write.writerow(['Order','Price','Quantity','Revenue'])
        for row in data:
            write.writerow(row)

def run_pipeline():
    file_data=extract('sales.csv')
    if file_data:
        processed=transform(file_data)
        load(processed)
    
run_pipeline()
