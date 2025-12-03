

alist = [10,20,30]
alist[0] = 100
print(alist)


atup = (10,20,30)
#atup[0]= 100
print(atup)


# typecasting - converting from one object to another object
atup = (10,20,30)
alist = list(atup) # converting tuple to list
alist[0] = 100
atup = tuple(alist) # recoverting back to tuple
print(atup)


aset = {10,10,10,20,30,30,30}
print(aset)