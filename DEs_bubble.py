liss=[3,5,2,7,9]

for i in range(0,len(liss)):
    for j in range(i,len(liss)):
        if liss[i]<liss[j]:
            liss[i],liss[j]=liss[j],liss[i]

print(liss)

     
