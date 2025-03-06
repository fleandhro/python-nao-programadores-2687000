# Declare 4 variáveis do tipo numérica
a = int(input('Nro 1: '))
b = int(input('Nro 2: '))
c = int(input('Nro 3: '))
d = int(input('Nro 4: '))

nros = [a, b, c, d]

# Crie uma estrutura condicional para comparar dois números
if (a > 0) and (b > 0) and (c > 0) and (d > 0): 
# Se a condição for verdadeira, imprima na tela uma mensagem informando que a condição foi cumprida e informando o número de maior valor
  print(f'A condição foi cumprida. {nros} são números positivos.')
# Se a condição não for cumprida, imprima na tela uma mensagem informando que a condição é negativa e informe o número de maior valor

elif (a == 0) or (b == 0) or (c == 0) or (d == 0):
  print('Número 0 digitado.')

else:
  print('A condição não foi cumprida. Número(s) negativo(s) digitado(s).')

# Insira outras condições na estrutura condicional usando o elif
# Incremente a estrutura condicional já existente com expressões lógicas utilizando "and" ou "or"
# Crie uma estrutura condicional onde mais de uma condição seja verdadeira, e use apenas a palavra reservada "if"
