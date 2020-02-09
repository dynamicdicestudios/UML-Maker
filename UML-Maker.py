classes = []
methods = []
temp = []
no_spaces = ""
code = open("example.py", 'r')

for line in code:
    
    if "class" in line:
        name = []
        no_spaces = line
        no_spaces = no_spaces.strip()
        temp = no_spaces.split(" ")
        classes.append(temp[1])
        for index in classes[len(classes)-1]:
            if index != "(":
                name.append(index)
            else:
                break
        classes[len(classes)-1] = "".join(name)
        
    elif "def" in line:
        name = []
        no_spaces = line
        no_spaces = no_spaces.strip()
        temp = no_spaces.split(" ")
        methods.append(temp[1])
        for index in methods[len(methods)-1]:
            if index != "(":
                name.append(index)
            else:
                break
        methods[len(methods)-1] = "".join(name)

print("These are the classes in this file:")
for name in classes:
    print(name)

print("These are the methods in this file:")
for name in methods:
    print(name)


    
