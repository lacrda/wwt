import math
# import random
# todos_terr=[]

# class Player:
# 	def __init__(self, name):
# 		self.name=name
# 		self.territories=[]
# 	def add_terr(self,terr):
# 		self.territories.append(terr)


# class Terr:
# 	def __init__(self,terr,owner):
# 		self.terr=terr
# 		self.owner=owner
# 		self.id=len(todos_terr)
# 		todos_terr.append([terr,owner])

# lac = Player("Lacerda")
# a=Terr('toni',lac.name)
# b=Terr('cavalo',lac.name)
# deb = Player('Mozert')
# a1=Terr('Zitolandia',deb.name)
# b1=Terr('Lengo',deb.name)

# # sortear um território na lista de todos territórios
# round_terr = random.choice(todos_terr)
# print(todos_terr.index(round_terr))

# # sortear o território que será conquistado na lista de territórios de outros donos
# f = filter(lambda x: x[1]!=round_terr[1], todos_terr) 
# filtered_todos_terr = list(f)
# round_def = random.choice(filtered_todos_terr)
# print(round_def)

# print(todos_terr)
import random

# criando o mapa do jogo
t=[]  
s=[]
for i in range(1,3):
	for j in range(1,9):
		t.append([i,j])
# t.append(s)
# print(list(t))

game = {
'pos1': [[1, 1],[1, 2]],
'pos2': [[1, 3],[1, 4]],
'pos3': [[1, 5],[1, 6]],
'pos4': [[1, 7],[1, 8]],
'pos5': [[2, 1],[2, 2]],
'pos6': [[2, 3],[2, 4]],
'pos7': [[2, 5],[2, 6]],
'pos8': [[2, 7],[2, 8]],
'pos9': [[3, 1],[3, 2]],
'pos10': [[3, 3],[3, 4]],
'pos11': [[3, 5],[3, 6]],
'pos12': [[3, 7],[3, 8]]
}

# def getKeysByValue(dict, value):
#     listOfKeys = list()
#     listOfItems = dict.items()
#     for item in listOfItems:
#         if value in item[1]:
#             listOfKeys.append(item[0])
#     return  listOfKeys

initial_pos = {
	'pos1': 'lacerda',
'pos2': 'arthur',
'pos3': 'beto',
'pos4': 'kradeu',
'pos5': 'john',
'pos6': 'logato',
'pos7': 'grey',
'pos8': 'girafa',
'pos9': 'bloris',
'pos10': 'bruno',
'pos11' : 'pablo',
'pos12' : 'be',
}

g = dict()

for k,v in game.items():
	for x in v:
			g[str(x)]=initial_pos[k]

# print(g)

# sorteando o terr que irá atacar
atack = random.choice(t)
at = str(atack)
print('terr que atacará')
print(at)
gat = g[at]
print(gat)


# sorteando o território para ser derrotado. Precisa estar a 1 unidade de distancia,e não pode ser do mesmo owner
dx=3
dy=3
dt=2
i = 0

while dt>1:
	i+=1
	target = random.choice(t)
	df = str(target)
	gdf = g[df]
	if gat == gdf:
		# print('não pode atacar a si próprio')
		continue
	dx = (atack[0]-target[0])
	dy = (atack[1]-target[1])
	dt = abs(dx)+abs(dy)


print('tentativa'+str(i))
print(target)
print(gdf)

g[df]=g[at]

print(g)





