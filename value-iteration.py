# VALUE ITERATION

# estados=[1,2,3,4,5,6,7,8,9,10]
# probabilista 0,5 ficar no mesmo lugar e 0,5 para ir para o proximo estado
# direcoes N, S, L, O
# meta S5 -- r(S5)= 0

gama = 1
r = -1
epson = 0.0001

listaLeste = [[0.5, 0.5, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0.5, 0.5, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0.5, 0.5, 0, 0, 0, 0, 0, 0]]

listaNova = [[0]*10,[0]*10,[0]*10]
print('\n')
print(listaNova)
print('\n')

for i in range(0, len(listaLeste)):
    for j in range(0, len(listaLeste[i])):
        t = listaLeste[i][i]
        tn = listaLeste[i][j]
        print('t :', t) 
        print('tn :', tn)
        listaNova[i][j] = (t *(r + (gama*listaNova[i][i]))) + (tn *(r + (gama*listaNova[i][j])))


print(listaNova)



