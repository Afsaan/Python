import re
count = 0
pattern = re.compile(r'\d\d\d(-|.)\d\d\d(-|.)\d\d\d\d')
with open('data.txt' , 'r') as f:
    content = f.read()
    matches = pattern.finditer(content)
    print(matches)
    for match in matches:
        count = count + 1 
        print(match)

print(count)