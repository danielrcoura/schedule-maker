import json

arq = open('../assets/horarios.json', 'r').read()
horarios = json.loads(arq)

disciplinas = []

for horario in horarios:
    if ({'selected': False, 'name': horario['nome']} not in disciplinas):
        disciplinas.append(
            {'selected': False, 'name': horario['nome']})

arq = open('../assets/disciplinas.json', 'w')
arq.writelines(json.dumps(disciplinas))

arq.close()
