# Crie uma lista apenas com elementos numéricos
lista = [1,2,3,4,5]
print(lista)

# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
lista_all = ['nome', 2, True, [1,2,3], 1.75, False, 'brasil']
print(lista_all)

# Imprima na tela apenas os 5 primeiros elementos da lista
print(lista_all[:5])

# Crie um slice na lista para que imprima na tela os elementos de índice par
print(lista_all[0:7:2])

# Remova da lista o último item
lista_all.pop() 
print(lista_all)

# Insira na lista um novo item
lista_all.append('peru')
print(lista_all)

# Remova da lista um item específico
lista_all.remove(True)
print(lista_all)
