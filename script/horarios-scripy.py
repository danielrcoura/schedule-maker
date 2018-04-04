import re
import json

horarios = open('./horarios.csv', 'r').readlines()
matriz = []

for i in horarios:
    matriz.append(i.split(","))

disciplinas = []
regTurma = re.compile(r'-t[1-9]$')

for line in range(2, len(matriz)):
    for col in [2, 8, 14, 20, 26]:
        if (not matriz[line][col]):
            continue

        disc = {}
        disc_id = matriz[line][col]
        if (regTurma.search(disc_id)):
            disc['nome'] = disc_id[0:-3]
            disc['turma'] = disc_id[-1]
        else:
            disc['nome'] = disc_id
            disc['turma'] = 1

        disc['sala'] = matriz[line][col - 1]
        disc['professor'] = matriz[line][col + 1]
        disc['cat'] = matriz[line][col + 2]

        if (col == 2):
            disc['dia'] = 'seg'
        elif (col == 8):
            disc['dia'] = 'ter'
        elif (col == 14):
            disc['dia'] = 'qua'
        elif (col == 20):
            disc['dia'] = 'qui'
        elif (col == 26):
            disc['dia'] = 'sex'

        if (2 <= line <= 4):
            disc['horario'] = '7'
        elif (6 <= line <= 22):
            disc['horario'] = '8'
        elif (24 <= line <= 40):
            disc['horario'] = '10'
        elif (44 <= line <= 61):
            disc['horario'] = '14'
        elif (63 <= line <= 79):
            disc['horario'] = '16'
        elif (81 <= line <= 85):
            disc['horario'] = '18'
        elif (87 <= line <= 89):
            disc['horario'] = '20'

        disciplinas.append(disc)

arq = open('../assets/horarios.json', 'w')
arq.writelines(json.dumps(disciplinas))
arq.close()
