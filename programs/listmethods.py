alist = [45,34,56,32,56,32,56]
alist.append(49)
print("After appending:",alist)
alist.extend([56,43,45,43])
print("After extending:",alist)
alist.insert(1,100)
print("After inserting:",alist)
alist.pop(0)  # list.pop(index) : value at index will be removed
print("After pop operation :",alist)
alist.remove(100000) # 100 is the element in the list
print("after removing :",alist)

if 1000 in alist:
    alist.remove(1000) # 100 is the element in the list
    print("after removing :",alist)
else:
    print("not in list")

alist.reverse()
print("After reversing :",alist)

alist.sort()
print("sorting in ascending order:",alist)

alist.sort(reverse=True)
print("sorting in descending order :",alist)