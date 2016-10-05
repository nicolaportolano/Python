# The following script takes a list 'x' that contains the values of Apple stocks (or whatever you want). Each value occurred at a specific time of the day
# (say a new value is generated every minute). The script then calculates what is (or would have been) the best price to buy some stocks and the best price to then resell them. 
import random as r


        
x = [r.randint(15,100) for i in range(20)] # list of Apple stocks

print ()
print ("List of Apple Stocks: ")
print (x)
print ()


z = [] 
y = [] 

               
# The following calculates the quotient of each value of x divided by each following values and appends them to z     
index = 0
while index < len(x)-1:
    slc = x[index:]
    n = slc[0]
    res = z.append([str(round(n / float(i), 3)) for i in slc[1:]])
    index = index + 1


print ("list z: ")
print (z)
print ()


# The following creates a nested list (y) of [[dividend,divisors],...] that originated the quotients in z.
index1 = 0
while index1 < len(x)-1:
    slc2 = x[index1:]
    n1 = slc2[0]
    res = y.append([[n1,i] for i in slc2[1:]])
    index1 += 1


print("list y: ")
print (y) 
print()


# The following joins the lists in z into z2.
z2=[]
for i in z:
        z2 += i


print ("list z2: ")
print (z2)
print()


# The following joins the lists in y in y2.
y2 = []
for i in y:
        y2 += i


print ("list y2: ")
print (y2)
print()


# The following creates a dictionary {quotient:[dividend, divisor]}. 
finals = dict(zip(z2,y2))


print ("finals: ")
print (finals)
print()


# finds smallest quotient (key) in finals.
for i in finals:
        i = min(finals.keys(), key=float)
 
 
# transforms the element in finals with the smallest key in a tuple.
for ele in finals:
        if ele == i:
                best = ele, finals[ele]
                
# calculates profit as a percentage.
difference = (best[1][1] - best [1][0])
profit = round((difference / best [1][0])*100,2) 

print ()
print ("The best profit is %s%%, which is given by buying stocks at $%s and reselling them at $%s."%(profit, best[1][0], best[1][1]))
print ()


        
        


     
     
    

