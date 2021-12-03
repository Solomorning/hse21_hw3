files = ["SRR3414635.counts","SRR3414636.counts","SRR3414637.counts","SRR3414629.counts","SRR3414630.counts","SRR3414631.counts"]
AllDict= {}
for i in files:
    file = open(i, 'r')
    for line in file:
        x = line.find('\t')
        if line[:x] not in AllDict.keys():
            AllDict[line[:x]] = []
        AllDict[line[:x]].append(int(line[x + 1:]))
    file.close()
file = open("ALL.counts", 'w')
file.write('c1,c2,c3,r1,r2,r3\n')
for i in AllDict.keys():
    file.write(i)
    for j in AllDict[i]:
        file.write(','+str(j))
    file.write('\n')
