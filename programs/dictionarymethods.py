book = {"chap1":10 ,"chap2":20 ,"chap3":30}
# add new key-values to dictionary
book["chap4"] = 40
book["chap5"] = 50
book["chap6"] = 60
print(book)
# display individual value 
print(book["chap6"])
print(book["chap2"])
# display all the keys
print(book.keys())
# display values 
print(book.values())
# display key-value pairs 
print(book.items())
# remove key-value 
book.pop("chap1") # chap1-10 will be removed 
print(book)
book.popitem() # last key-value will be removd
print(book)
book = {"chap1":10 ,"chap2":20 ,"chap3":30}
newbook = {"chap4":40}

book.update(newbook)
print(book)