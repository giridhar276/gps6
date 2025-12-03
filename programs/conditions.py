
# simple if
if 1 < 2 :
    print("true")
    print("inside if")
    print("still inside if")


name = "python"
if name.islower():
    print("string is lower")


if name.startswith("p"):
    print("string starts with p")

# if-else
name = "python"
if name.islower():
    print("string is lower")
else:
    print("string is upper")


# if-elif-elif-elif-elif-else
lang = input("Enter any lang:")
if lang == "python":
    print("you entered python")
elif lang == "java":
    print("you entered java")
elif lang == "unix":
    print("you entered unix")
else:
    print("you entered something else")