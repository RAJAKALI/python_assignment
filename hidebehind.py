n=int(input('number of test cases:'))#number of test cases
lst=[] #list for test case output
for c in range(n): #loop for testcases     
    n,k =map(int,input('enter no players and height of Gi-hun & Ali:').split())# map and split for space seperated inputs
    p=list(map(int,input('enter players height:').split()[:n]))#taking players height with space seperated by using map and split and appending those values to the list
    c=0 #counter for number of players whose height is greater than gi-hun and ali
    for i in p:#taking every players height to comaper with gihun and ali
        if(i>k):# condition for if this player height is greater than gihun and ali
            c+=1 #if the players height is greater than them we increase the counter +1
    lst.append(c)# at final we will found number of players greater than the gihun and ali and appending each test case output to the list
print('number of players who need to get shot:')
for i in lst:
    print(i)#ouput 
