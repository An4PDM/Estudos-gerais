#Faça um Programa que peça dois números inteiros e um número real. Calcule e mostre:
#a) o produto do dobro do primeiro com metade do segundo;
#b) a soma do triplo do primeiro com o terceiro;
#c) o terceiro elevado ao cubo.

num1 = int(input('Digite um numero inteiro: '))
num2 = int(input('Digite um numero inteiro: '))
num3 = float(input('Digite um numero real: '))
a = (num1*2)*(num2/2)
b = (num1*3) + num3
c = num3**3
print(a)
print(b)
print(c)

