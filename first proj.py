name = input("name")
eachWord = name.split()
totalname = ""
for word in eachWord:
    totalname += (word[0].upper() + ".")
print("Your initials are " + totalname)
