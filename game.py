import math
import random

# criando o mapa do jogo
t=[]  
s=[]
for i in range(1,4):
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
'grey': 'olive',
'girafa': 'brown',
'bloris': 'orange',
'bruno': 'pink',
'pablo' : 'cyan',
'be' : 'purple',
}

g = dict()

for k,v in game.items():
	for x in v:
			g[str(x)]=[initial_pos[k],colors[initial_pos[k]]]

def return_g():
	return g

def return_colors():
	return colors
a = return_g()
print(a)
