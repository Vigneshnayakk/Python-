n=int(input('Enter the number of stages:'))
temp=1
for i in range(n-1,-1,-1):
    print(i*' ' + temp * '* ')
    temp+=1
