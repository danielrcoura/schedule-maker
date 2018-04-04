import json

arq = open('../assets/horarios.json', 'r').read()
horarios = json.loads(arq)

disciplinas = {}

for horario in horarios:
    disciplinas[horario['nome']] = {'selected': False, 'turma': 1}

arq = open('../assets/disciplinas.json', 'w')
arq.writelines(json.dumps(disciplinas))

arq.close()
