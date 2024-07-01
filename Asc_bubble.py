lis=[5,3,4,2]

for i in range(0,len(lis)):
    for y in range(i,len(lis)):

        if lis[i]>lis[y]:
            lis[i],lis[y]=lis[y],lis[i]

print(lis)
       