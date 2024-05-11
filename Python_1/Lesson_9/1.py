#Working with Strings
# len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), join()
f = "Course in Video Python"
print(f[1:15])#1-14,. without 15
print(f[1:15:2])#jumping 2 and 2
print(f[1::2])#I don't know the end
print("-"*100)
#--------------------
print("Length: ",len(f))
print("Count with: ",f.count("o"))
print("Count with Slicing: ",f.count("o", 0, 13))
print("Find: ",f.find("deo"))
print("Find: ",f.find("xyz"), "don't found")
print("-"*100)
#----------------------
print('Course' in f)
print("-"*100)
#----------------------
newF = f.replace("Python", "Javascript")#It doesn't modify original variable, that's why is better to create a new variable here
print(f.upper())
print(f.lower())
print(f.capitalize())
print(f.title())
print("-"*100)
#----------------------
j = "   Learn Python!  "
print("With all spaces: ", j)
print(len(j))
k = j.strip() ## .rstript - just right,        .lstrip() just left
print("Without spaces",len(k))#take spaces
print("-"*100)
#----------------------
print("Split: ",f.split())
print("Split with Length: ",len(f.split()))#Divide in new small lists
justEachWord = f.split()
print("Split in the first small list: ",justEachWord[0])#Divide in new small lists
courseWord = justEachWord[0]
print(courseWord)
print(justEachWord)
print("-"*100)
print("Join")
print("$".join(justEachWord))