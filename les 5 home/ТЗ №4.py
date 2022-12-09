string ='rrrrrrssssasawwwwwwwwwiiii'
count = 1
a = ''
for i in range(len(string) - 1):
    if string[i] == string[i + 1]:
        count += 1
        if i == len(string) - 2:
            print(count, string[i], sep='')
    else:
        if i == len(string) - 2 and string[i] == string[-1]:
            count += 1
        elif i == len(string) - 2:
            a = string[-1]
        if count > 1:
            print(count, end='')
        count = 1
        print(string[i], end='')
print(a)


