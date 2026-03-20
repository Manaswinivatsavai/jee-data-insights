try:
    with open('numbers.txt','w') as wp:
        wp.write(str(10)+'\n')
        wp.write(str(20)+'\n')
        wp.write('abc'+'\n')
        wp.write(str(30)+'\n')
        wp.write(str(40)+'\n')
        print("Data added-->Verify")
except TypeError:
    print("error")

