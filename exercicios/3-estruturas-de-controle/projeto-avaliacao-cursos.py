# Nesse desafio você verificará dentro de uma lista se o item estar contido nela, caso verdadeiro deverá imprimir na tela essa informação, além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.
# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning
# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas
# 3. Crie um dicionário vazio para armazenar a nota do curso
# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista
# 5. Se o curso estiver na lista, solicite uma nota para avaliação
# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota

cursos_linkedin = ['C++', 'Python', 'Cobol', 'Pascal', 'Basic']

curso_java = 'Java'
curso_pascal = 'Pascal'
curso_basic = 'Basic'

avaliacoes = {}

if curso_java in cursos_linkedin:
  print(f'Curso {curso_java} no catálogo. Por favor, avalie.')
  avaliacoes[curso_java] = int(input('Nota (0 a 5): '))
else:
  print(f'Curso {curso_java} não listado.')

if curso_pascal in cursos_linkedin:
  print(f'Curso {curso_pascal} no catálogo. Por favor, avalie.')
  avaliacoes[curso_pascal] = int(input('Nota (0 a 5): '))
else:
  print(f'Curso {curso_pascal} não listado.')

if curso_basic in cursos_linkedin:
  print(f'Curso {curso_basic} no catálogo. Por favor, avalie.')
  avaliacoes[curso_basic] = int(input('Nota (0 a 5): '))
else:
  print(f'Curso {curso_basic} não listado.')

print('')
print('Avaliações: ')
print(avaliacoes)

