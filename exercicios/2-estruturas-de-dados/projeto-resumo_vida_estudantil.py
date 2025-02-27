# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
# 2. Armazene esses dados em um dicionário
# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.

estudante = {}

estudante['nome'] = input('Aluno: ')
estudante['ano_linkedin'] = int(input('Ano inscrição no LinkedIn: '))
estudante['ano_atual'] = int(input('Ano atual: '))
cursos = input('Cursos realizados: ')

estudante['cursos'] = cursos.split(', ')

anos_transcorridos = estudante['ano_atual'] - estudante['ano_linkedin']
total_cursos = len(estudante['cursos'])

print(f"{estudante['nome']}, desde {estudante['ano_linkedin']}, \
há {anos_transcorridos} anos, você concluiu {total_cursos} cursos, \
sendo o primeiro {estudante['cursos'][0]}, \
e o último {estudante['cursos'][-1]}.")