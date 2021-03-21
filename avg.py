input_string = input("Enter a list element separated by comma ")
lis1  = input_string.split(',')
print(lis1)
total=0
count=0
for i in lis1:
    total+=int(i)
    count+=1
print('average is : ',total/count)    
    
