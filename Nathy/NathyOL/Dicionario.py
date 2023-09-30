dicionario = {
    'Nome': 'Alan',
    'Idade': '18',
    'ID' : '789'
}

#Verificar qual o valolr da chave "Nome"
print(dicionario['Nome'])

#Elemento que nao existe = ERRO
#print(dicionario['CPF'])

#Saber se um elemento existe
print('Nome' in dicionario)

#Valores do dicionario
print(dicionario.values())