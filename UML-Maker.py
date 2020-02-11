import matplotlib.pyplot as plt 

classes = []
methods = []
var = []
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

    elif "=" in line:
        if len(line.lstrip()) == len(line):
            name = []
            no_spaces = line
            no_spaces = no_spaces.strip()
            temp = no_spaces.split(" ")
            var.append(temp[0])
            print(var)
            for index in var[len(var)-1]:
                if index != "=":
                    name.append(index)
                else:
                    break
            var[len(var)-1] = "".join(name)
            
"""print("These are the classes in this file:")
for name in classes:
    print(name)

print("These are the methods in this file:")
for name in methods:
    print(name)

print("These are the variables in this file:")
for name in var:
    print(name)"""

fig = plt.figure(dpi=80)
ax = fig.add_subplot(1,1,1)
table_data=[
    [],
    [var],
    [methods]
]

if len(classes) == 0:
    table_data[0] = "N/A"
else:
    table_data[0] = classes[0]

"""for name in var:
    table_data[1].append(name)

for name in methods:
    table_data[2].append(name)"""

table = ax.table(cellText=table_data, loc='center')
table.set_fontsize(14)
table.scale(1,4)
ax.axis('off')
plt.show()
