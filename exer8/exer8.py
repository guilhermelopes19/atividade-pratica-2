#Alunos
#Guilherme Souza Lopes - 072320015
#Sara Stephanie Costa - 0723200

# O seguinte codigo recebe uma temperatura 
# em graus Fahrenheit e converte para graus Celsius

grausF = float(input('Digite a temperatura em ºF: ')) # recebe uma temperatura em ºF
grausC = 5 * ((grausF - 32) / 9) # converte a a temperatura grausF para ºC

print(f'A temperatura {grausF:.1f}ºF equivale a {grausC:.1f}ºC') # imprime a temperatura em ºF e ºC
