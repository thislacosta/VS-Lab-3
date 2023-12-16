import random
lst = [ ]
for i in range(10):
    number = random.randint(0, 101) 
    lst = lst + [number]
print("lst = ", lst)
f = open('file.txt', 'w')
s=str(len(lst))
f.write(s + '\n')
for i in lst:
    s = str(i) 
    f.write(s + ' ')
f.close()
f=open('file.txt','r+')
s=f.readline()
lst2=[ ]
for line in f:
    strs=line.split(' ')
    print('strs=',strs)
    for s in strs:
        if s!='':
            lst2=lst2+[int(s)]
print('lst2=',lst2)
b=[ ]
for x in lst2:
    if x>55:
        b.append(x)
print('b=:',b)
p=0
for i in b:
    p=p+i
print('p=:',p)
