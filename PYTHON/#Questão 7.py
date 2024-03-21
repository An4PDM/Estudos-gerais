#Questão 7
n1 = int(input('Digite valor 1: '))
n2 = int(input('Digite valor 2: '))
n3 = int(input('Digite valor 3: '))
média = (n1 + n2 + n3)/3
print('A média dos valores é igual a ', média)
if (n1>n2 and n1>n3):
    print('O maior valor é', n1)
elif (n2>n1 and n2>n3):
    print('O maior valor é', n2)
else:
    print('O maior valor é', n3)

if (n1<n2 and n1<n3):
    print('O menor valor é', n1)
elif (n2<n1 and n2<n3):
    print('O menor valor é', n2)
else:
    print('O menor valor é', n3)
    