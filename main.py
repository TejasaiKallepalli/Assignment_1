import statistics
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]  #initialisation of list
ages.sort() #function for sorting list
print(ages)
m=min(ages) #function for finding minimun of ages
n=max(ages) #function for finding minimun of ages
ages.append(m) #function for appending minimun of ages
ages.append(n) #function for appending minimun of ages
print(ages)
print("Median of Ages is %s:"% statistics.median(ages)) #function for finding median of ages
print("Average of Ages is %s" % statistics.mean(ages)) #function for finding aerage of ages
range=n-m
print("range of ages is %s" %range) #Printing range of ages



