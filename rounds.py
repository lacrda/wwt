import math
import random
import random
from models import Terr

def teste(json):
	all_terr = list(json)
	print(all_terr[28])

# mapa do jogo
t=[]  
s=[]
for i in range(1,4):
	for j in range(1,9):
		t.append([i,j])

def go_round():
	# sorteando o terr que irá atacar
	atack = random.choice(t)
	at = str(atack)
	print('terr que atacará:')
	print(at)

	# sorteando o território para ser derrotado. Precisa estar a 1 unidade de distancia,e não pode ser do mesmo owner
	dx=3
	dy=3
	dt=2
	i = 0

	while dt>1:
		i+=1
		target = random.choice(t)
		df = str(target)
		if df == at:
			print('não pode atacar a si próprio')
			continue
		dx = (atack[0]-target[0])
		dy = (atack[1]-target[1])
		dt = abs(dx)+abs(dy)


	print('tentativa'+str(i))
	print(target)
	terrs = [at,df]
	return terrs

	# g[df]=g[at]
 
