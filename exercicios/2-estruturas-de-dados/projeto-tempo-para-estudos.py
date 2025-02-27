# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:
# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;
# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
# 3. Crie uma variável chamada "total_horas" e, usanod o método input(), solicite a média de horas estudada por dia;
# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;
# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.

nome = str(input('Seu nome: '))
total_dias = int(input('Dias de estudo por semana: '))
total_horas = int(input('Horas de estudo por dia: '))
curso = str(input('Seu curso: '))
horas_semanais = total_horas * total_dias

print(f'{nome}, você dedicou {horas_semanais} horas semanais \
ao seu curso de {curso}.')