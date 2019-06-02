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
for i in range(1,7):
	for j in range(1,9):
		t.append([i,j])
# t.append(s)
# print(list(t))

game = {'pos1': [[1, 1],[1, 2],[2, 1]],
'pos2': [[2, 2],[3, 1],[3, 2]],
'pos3': [[4, 1],[4, 2],[5, 2]],
'pos4': [[5, 1],[6, 1],[6, 2]],
'pos5': [[1, 3],[1, 4],[2, 4]],
'pos6': [[2, 3],[3, 3],[3, 4]],
'pos7': [[4, 3],[4, 4],[5, 3]],
'pos8': [[5, 4],[6, 3],[6, 4]],
'pos9': [[1, 5],[1, 6],[2, 5]],
'pos10':[[2, 6],[3, 5],[3, 6]],
'pos11' :[[4, 5],[4, 6],[5, 6]],
'pos12' :[[5, 5],[6, 5],[6, 6]],
'pos13' :[[1, 7],[1, 8],[2, 8]],
'pos14' :[[2, 7],[3, 7],[3, 8]],
'pos15' :[[4, 7],[4, 8],[5, 7]],
'pos16':[[5, 8],[6, 7],[6, 8]]}

# def getKeysByValue(dict, value):
#     listOfKeys = list()
#     listOfItems = dict.items()
#     for item in listOfItems:
#         if value in item[1]:
#             listOfKeys.append(item[0])
#     return  listOfKeys

initial_pos = {
	'pos1': 'lacerda',
'pos2': 'Mozert',
'pos3': 'Terezinha',
'pos4': 'arthur',
'pos5': 'pedro',
'pos6': 'reb',
'pos7': 'migs',
'pos8': 'dona vera',
'pos9': 'kradeu',
'pos10': 'john',
'pos11' : 'rapha',
'pos12' : 'comp1',
'pos13' : 'comp2',
'pos14' : 'comp3',
'pos15' : 'comp4',
'pos16': 'comp5'
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





