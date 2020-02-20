import json
data = open('test_data.json', mode='r', encoding='windows-1251')
json_data = json.load(data)

def conv(c):
    l = []
    if len(c) == 7:
        l.extend([int(c[0:2]), int(c[5:7])])
    elif len(c) == 6:
        l.extend([int(c[0]), int(c[4:6])])
    elif len(c) == 5:
        l.extend([int(c[0]), int(c[4])])
    elif len(c) == 2:
        l.extend([int(c[0:2])])
    elif len(c) == 1:
        l.extend([int(c[0])])
    return l

def list_up(l):
    a = l[0]
    b = l[len(l)-1]
    for i in range(a+1, b):
        l.insert(i-l[0], i)
    return l

#for olymp in json_data:
for i in range(96, 140):
    olymp = json_data[i-43]
    c = olymp.get('Class')
    print('\n',olymp.get('ID'), i, '\t', c, type(c))
    print(conv(c))
    #print(list_up(conv(c)))