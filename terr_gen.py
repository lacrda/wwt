#  		uerj:{lat: -22.911, lng:  -43.237},
# 	    praça niteroi:{lat: -22.914, lng:  -43.234},
#          pde fcisoc lana {lat: -22.918, lng:  -43.243},
#          chicken {lat: -22.920, lng:  -43.260},
#          zoo {lat: -22.915, lng:  -43.262},
#          tunel nrosa {lat: -22.910, lng:  -43.258}


#    terrs 0: limit_sup=-22.910 lat_inf = -22.912 
#    linha 1: lat_sup = -22.912 lat_inf = -22.915 
#    linha 2: lat_sup = -22.915 lat_inf = -22.917 
#    linha 3: lat_sup = -22.917 lat_inf = -22.919
#    linha 4: lat_sup = -22.919 limite_inf = -22.920

#    limite_wes= -43.262
#    limite_eas= -43.234

import random
chosen =[234,263]
b=range(234,263)
while len(chosen) < 7:
	a1 = random.choice(b)
	if a1 in chosen:
		continue
	else:
		chosen.append(a1)

chosen.sort()

def xcoord(list):
	coord=[]
	rng = range(0,len(list)-1)
	for x in rng:
		coord.append([
			[(-43-(list[x]/1000)),-22.912],
			[(-43-(list[x+1]/1000)),-22.912],
			[(-43-(list[x]/1000)),-22.910],
			[(-43-(list[x+1]/1000)),-22.910]
			])
	print(rng)
	print(coord)

xcoord(chosen)