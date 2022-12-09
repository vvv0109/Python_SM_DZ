data = open('initial.txt', 'r')
str_list=[]
for line in data:
    str_list.append(line)
data.close()
str_list = [word for line in str_list for word in line.split()]
stringVal='e5'
str_list=[ x for x in str_list if not stringVal in x ]
print(*str_list)
#data.writelines()