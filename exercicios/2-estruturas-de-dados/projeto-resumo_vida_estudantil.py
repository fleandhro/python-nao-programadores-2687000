# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
# 2. Armazene esses dados em um dicionário
# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.

nome = str(input('Nome: '))
ano_linkedin = int(input('Ano que conheceu o LinkedIn: '))
ano_atual = int(input('Ano atual: '))
cursos_realizados = str(input('Últimos 3 cursos concluídos: '))

print(f'{nome}, você entrou no LinkedIn em {ano_linkedin}, há {ano_atual - ano_linkedin} anos atrás, e já concluiu x cursos, sendo o primeiro x e o último y')