import math
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
'pos1': ["[1, 1]","[1, 2]"],
'pos2': ["[1, 3]","[1, 4]"],
'pos3': ["[1, 5]","[1, 6]"],
'pos4': ["[1, 7]","[1, 8]"],
'pos5': ["[2, 1]","[2, 2]"],
'pos6': ["[2, 3]","[2, 4]"],
'pos7': ["[2, 5]","[2, 6]"],
'pos8': ["[2, 7]","[2, 8]"],
'pos9': ["[3, 1]","[3, 2]"],
'pos10': ["[3, 3]","[3, 4]"],
'pos11': ["[3, 5]","[3, 6]"],
'pos12': ["[3, 7]","[3, 8]"]
}

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

colors = {
'lacerda': 'gray',
'arthur': 'blue',
'beto': 'yellow',
'kradeu': 'red',
'john': 'green',
'logato': 'white',
'grey': 'black',
'girafa': 'brown',
'bloris': 'orange',
'bruno': 'pink',
'pablo' : 'cyan',
'be' : 'purple',
}

g = dict()

for k,v in game.items():
	for x in v:
			g[str(x)]=initial_pos[k]

# sorteando o terr que irá atacar
atack = random.choice(t)
at = str(atack)
# print('terr que atacará')
# print(at)
gat = g[at]
# print(gat)

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


# print('tentativa'+str(i))
# print(target)
# print(gdf)

g[df]=g[at]

def return_g():
	return g


a = return_g()
print(a)
# from models import Owners
# import app
# from flask import Flask, render_template, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import create_engine, func
# # Salvar no db na tabela Terr os terr com posições e owner
# lacerda = Owners('lacerda', colors['lacerda'],2)
# db = SQLAlchemy(app)
# db.session.add(lacerda)
# db.session.commit()

