l=[12,1,9,2,6,5,7,10,15,11,3,8,4]
for i in range(len(l)):
    for j in range(len(l) - 1):
        if l[j] > l[i]:
            l[i], l[j] = l[j], l[i]
        print(l),
        print("")