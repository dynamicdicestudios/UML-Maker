import matplotlib.pyplot as plt 
def find_info(lang, file):
    if lang == "python":
        #variables used for going through data
        classes = []
        methods = []
        var = []
        temp = []
        no_spaces = ""

        #file that is being looked through
        code = open(file, 'r')

        for line in code:
            if "class" in line:
                name = []
                no_spaces = line #stores the line in a variable for it to be mutable
                no_spaces = no_spaces.strip() #gets rid of unnecessary spaces
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

table = ax.table(cellText=table_data, loc='center')
table.set_fontsize(14)
table.scale(1,4)
ax.axis('off')
plt.show()
