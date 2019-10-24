#define dictionary
details = {"name": "afsaan", 'age' :22, "gender":"male"}

#how to acess the value from the dic
value = details["name"]  # 1st method
value1 = details.get("name")  #2nd method
print(value,value1)

#how to change the value of the key in the dic
details["name"] = "khan"

# how to add the new key in the dictionary
details["fav_lan"]="python"

print(details)

# for loop for the dic
for x in details:   # name of all the keywords
    print(x)

print("\n")
for x in details:
    print(x,details[x])

print("\n")

# if you want only to acces the values
for x in details.values():
    print(x)

for x,y in details.items():
    print(x,y)



