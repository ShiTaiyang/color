#default:
#gamma = 2.0
#x = 0.3, y = 0.3
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

singledata = [x[0] for x in dat2]
sd = singledata

sdmin = min(sd)
sdmax = max(sd)

nd = [(x-sdmin)/(sdmax-sdmin) for x in sd]

#print(len(nd))=1280

#nddiv = []
#i = 1
#for i in range(0,256):

#   nddiv.append(nd[i*5])

gamma = 2.0
ga=[]

for j in range(0,len(nd)):
    ga.append((j/len(nd))**gamma)

print(ga)
print(len(ga))

mpl.plot(nd,ga)
mpl.show()





        


