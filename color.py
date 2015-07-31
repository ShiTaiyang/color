#default:
#gamma = 2.0
#x = 0.3, y = 0.3
############
import matplotlib.pyplot as mpl
import numpy as np
#getData
table = open('mod.r.pl','r')

#print (table.readline())    

dat = []
for line in table:
#    print(line)
    vals = line.strip().split(' ')[1:]
    dat.append(vals)


dat2=[]
for line in dat:
    dat2.append(list(map(float,line)))



dat2.sort(key = lambda x:x[2])

#default x= 0.3, y= 0.3, gamma = 2.0
#X = 300, Y = 300, Z = 400

sg1 = [x[0] for x in dat2]
sg2 = [x[1] for x in dat2]
sg3 = [x[2] for x in dat2]
sd=[]
for i in range(len(dat2)):
    sd.append(sg1[i]+sg2[i]+sg3[i])

print(sd)
sdmin = min(sd)
sdmax = max(sd)

nd = [(x-sdmin)/(sdmax-sdmin) for x in sd]



#generate gamma
gamma = 2.0
ga= []

for j in range(256):
    ga.append((j/256)**gamma)
    
#find a range, just trying
var = 0
for p in range(len(nd)):

    var+=(nd[p] - (p/len(nd))**2)**2

var = var/len(nd)
var = var ** (1/2)
#choose the points
print(var)

for x in nd:        
    if x < (1/256)**gamma-var or x > 1+var:#no use#
            nd.remove(x)

ch=[]
y=[]
for i in range(256):
    y.append((i/256)**gamma)
    for j in range(len(nd)):
        if nd[j] >= (i/256)**gamma:
            ch.append(nd[j])
            break

print(ch)
#print(len(ch))
mpl.figure(1)
mpl.subplot(211)
mpl.title('result of map to gamma')
mpl.plot(ch,'r')
mpl.subplot(212)
mpl.title('gamma of 2.0')
mpl.plot(ga,'b')

mpl.figure(2)
mpl.plot(ch,ga,'g',y,y,'r--')

mpl.show()






        


