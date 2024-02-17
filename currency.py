'''
* logic for this code is that i observe from obser from our currency notations is
* we have three types in indian currency numbers
first one is.. for 100 and below we doest use any comma(notations)
* second is if the number is even if it is 1000,100000,1000000 the output shoud be (1,)(000) (1,)00,(000)... so
i found that for even numbers the first and last three numbers are seperated by notations and
middle number sperated by notations after every two numbers
*same for odd numbers first two numbers and last two numbers and middle numbers after every two postions notations are required (10,)(000)  (10),00,(000)

by this logic i wrote this program
'''

n=int(input("enter the number:")) #input for number
n=str(n) #converting the integer to str to perform length and list operations on the number
l=len(n) #lenght of the number
lst=[] #list for numbers
c=0 #counter for middle numbers notation for even number
r=0 #counter for end point for middle numbers
re=1 #counter for odd numbers
if(l<=3): #if numbers are below 100 we print the numbers as it is
    print(n)
elif(l%2==0): #if the number greater than 100 and even
    lst.append(n[:1]+',') #for first number shoud be seperated by notation it is comman for all even numbers and appending to list
    for i in (n[1:]): #loop for middle numbers
        c=c+1 #counter for middle numbers 
        r=r+1 #counter for middle numbers end point
        if(r==(l-3)): #if loop reached to the last three number loop should be stop
            break
        lst.append(i) #appending the number to list
        if(c==2): #if counter c is equals to 2 it should append notation (because for evey two number we need noation for middle numbers)
            lst.append(',')
            c=0 #making zero so that we can perform another notation for middle numbers if the counter c is equals to 2
    lst.append(n[-3:]) #appending last 3 digits to list
    print("".join(lst)) #converting list to string for ouput
else:
    lst.append(n[:2]+',') #here for odd we take first two and last three to list and everying is same as even
    for i in (n[2:]):
        c=c+1
        re=re+1
        if(re==(l-3)):
            break
        lst.append(i)
        if(c==2):
            lst.append(',')
            c=0
    lst.append(n[-3:])
    print("".join(lst))


