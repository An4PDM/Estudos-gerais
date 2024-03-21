#Usamos o for quando sabemos a quantidade de elementos a serem repetidos.
lista = ['maçã', 'limão', 'laranja']
for i in lista:
    print(i)
# for i in lista ( o i é a iteração)

for contador in range (0,5):
    print(contador)
#range para sequência de números

seq = [1,2,3,4,5,6,7,8,9,10]
for num in seq:
    if (num % 2 == 0):
     print(num)
# o 'num' é como se fosse CADA ELEMENTO da lista.

for pares in range (0,101,2):
    print(pares)
#O último número representa 'quantas vezes a sequência é pulada'.

for letras in ('Ciências'):
    print(letras)
#Strings também são sequências.
    
lista = [1,2,3,4,5,5]
for i in lista:
    if (i == 5):
        print('VALOR ENCONTRADO.')

for palavra in 'PYTHON':
    if (palavra == 'H'):
        continue
    print(palavra)

for palavra in 'python':
    if (palavra == 'h'):
        break
    print(palavra)

for palavra in 'Python':
    if (palavra == 'h'):
        pass
    print(palavra)