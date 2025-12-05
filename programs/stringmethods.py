name = "python programming"
# string[start:stop:step]
print(name)
print(name[0])
print(name[1])
print(name[0:4])
print(name[8:12])
print(name[0:18:2])
print(name[0:18:3])


name = "python programming"
print(name.capitalize())
print(name.upper())
print(name.isupper())
print(name.lower())
print(name.islower())
print(name.replace("python","java"))
print(name.find("abc")) # if substring is not found.. it returns -1
print(name.find("hon")) # if substring is found... it returns the starting index of substring
name.