lista_compras=["frutas", "pao", "carne", "arroz", "crockeros"]

print("Hoje vou comprar no mercado: ", lista_compras)
print(type(lista_compras))
print("A quantidade de elementos em minha lista eh", lista_compras)

lista_compras.append("feijao")
print(lista_compras)

lista_compras.sort()
print(lista_compras)

#tirando o biscoito
lista_compras.remove("crockeros")
print(lista_compras)

#Indicar o 3 elemento da lista
print("O 3 elemento eh o: " , lista_compras[2])

#Indicar o ultimo elemento
print("o ultimo elemento eh: ", lista_compras[-1])

#Remover o 4 elemento
print("O 4 elemento removido foi: ", lista_compras.pop(4))

#Exibir os 3 primeiros elementos
print("Exibir os 3 primeiros elementos: ", lista_compras[0:3])
 





