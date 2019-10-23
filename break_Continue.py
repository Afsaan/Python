# break
name = ['rahul','afsaan','nadu','sanket']

for i in name:
    if i == "afsaan":
        break
    print(i)


j=0
while j < len(name):
    print(name[j])
    if name[j] == "nadu":
        break
    j=j+1


# continue
skills = ['machine leanring','data analyst','Deep learning','computer vision']

for i in skills:
    print(i)
    if i == "Deep learning":
        continue
print("\n")
print("while \n")
j=0
while j < 5:
    j=j+1
    if j ==2:
        continue
    print(j)


    
