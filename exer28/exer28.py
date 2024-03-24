#Alunos
#Guilherme Souza Lopes - 072320015
#

# O seguinte programa recebe os coeficientes de uma equação 
# do segundo grau e imprime o valor das suas raízes reais
# se existirem

import sys

print('Calcular o valor de x de uma equação do segundo grau')

coefA = float(input("Digite o coeficiente a: ")) # recebe o valor do coeficiente a

if coefA == 0:#verifica se coeficiente a é igual a 0
    print('O coeficiente a deve ser maior que 0!') #imprime que a deve ser maior que 0
    sys.exit()#Encerra o programa

coefB = float(input("Digite o coeficiente b: ")) # recebe o valor do coeficiente b
coefC = float(input("Digite o coeficiente c: ")) # recebe o valor do coeficiente c

print('-'*20)
print(f'{coefA}x² + {coefB}x + {coefC} = 0') # imprime a equacao quadratica com os valores digitados anteriormente
print('-'*20)

def calcularValorXEquacaoQuadratica(a, b, c): # função que recebe os coeficientes a, b e c e calcula as raizes da equacao do segundo grau
    delta = b**2 - 4 * a * c # inicializa a variavel com o valor  de delta 
    x1 = (-b + delta**(1/2))/(2 * a) # inicializa a variavel com o valor da primeira raiz da equacao
    x2 = (-b - delta**(1/2))/(2 * a) # inicializa a variavel com o valor da segunda raiz da equacao

    if delta > 0: # Verifica se delta é positivo
        print(f'x1 = {x1}') # imprime o valor da primeira raiz
        print(f'x2 = {x2}') # imprime o valor da segunda raiz
    elif delta == 0: # verifica se delta é igual a zero
        print(f'x = {x1}') # imprime o valor da primeira raiz pois se delta = 0 entao x1 == x2
    else:
        print('Delta negativo!')# imprime que o delta é negatico
calcularValorXEquacaoQuadratica(coefA, coefB, coefC) # chamada da calcularValorXEquacaoQuadratica
