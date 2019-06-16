#  		uerj:{lat:- -22.911, lng:  -43.237},
# 	    praça niteroi:{lat:- -22.914, lng:  -43.234},
#          pde fcisoc lana {lat:- -22.918, lng:  -43.243},
#          chicken {lat:- -22.920, lng:  -43.260},
#          zoo {lat:- -22.915, lng:  -43.262},
#          tunel nrosa {lat:- -22.910, lng:  -43.258}


#    terrs 0: limit_sup=-22.910 lat_inf = -22.912 
#    linha 1: lat_sup = -22.912 lat_inf = -22.915 
#    linha 2: lat_sup = -22.915 lat_inf = -22.917 
#    linha 3: lat_sup = -22.917 lat_inf = -22.919
#    linha 4: lat_sup = -22.919 limite_inf = -22.920

#    limite_wes= -43.262
#    limite_eas= -43.234
import random

lat = "-22."
lng = "-43."
lat_lines = []

c = [-1,0,1]
v=[]
for v in range(32):
	v= random.choice(c)


points = {}
d = [910,913,916,919]
l = [234,238,242,246,250,254,258,262,266]
l.sort(reverse=True)
dlen = len(d)
llen = len(l)
iter = 0
for i in range(dlen):
	for j in range(llen):
		c1 = random.choice(c) 
		points['p'+str(iter)]="{lat:-22."+str(d[i]+c1)+", lng: -43."+str(l[j]+c1)+"}"
		iter+=1
print(points)
for i in range(0,36):
	if i%37==0:
		continue
	if i>24:
		break
	# print(points['p'+str(i-1)])
	print("var terr"+str(i-1)+"=["+points['p'+str(i-1)]+","+points['p'+str(i)]+","+points['p'+str(i+9)]+","+points['p'+str(i+8)]+"];")

# chosen_b=([234,910],[263,918])
# chosen_b = list(chosen_b)
# iter = 0
# for x in [0,1,2,3,4]:
# 	chosen=[]
# 	b=range(234,264)
# 	b=list(b)
# 	bb = range(len(b)-2)
# 	bb = list(bb)
# 	while len(chosen) < 9:
# 		a1 = random.choice(bb)
# 		a2 = b[a1]
# 		b.pop(a1)
# 		bb.pop(-1)
# 		chosen.append([a2,d[x]])
# 	chosen.sort(reverse=True)
# 	print(chosen)
	# clen = range(chosen)
	# for c in clen:
	# 	points['p'+c]=[chosen[c]]

# chosen_b.sort(reverse=True)
# a=range(len(chosen_b))
# a = list(a)
# for ab in a:
# print(points)
