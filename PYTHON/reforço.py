#Questão 1
ano = float(input('Digite o ano: '))
resto = ano % 4
comprov = ano % 100
comprov2 = ano % 400
print(resto)
print(comprov)
print(comprov2)
if (resto == 0 or comprov2 == 0):
    print('ano bissexto')
    if (comprov == 0):
        print('ano não bissexto')
else:
    print('Esse ano não é bissexto')
 
#Questão 2
senha = float(input('Crie uma senha: '))
conf = float(input('Confirme a senha: '))
if (senha == conf):
    print('Senha confirmada')
else:
    print('Erro de confirmação')
 
#Questão 3
a = float(input('Digite um valor para a: '))
b = float(input('Digite um valor para b: '))
c = float(input('Digite um valor para c: '))
d = b**2 + (4*a*c)
print(d)
if (d>0):
    print('Duas raízes')
elif (d == 0):
    print('Uma raíz real')
else:
    print('Não possui raízes')
 
#Questão 4
idade = int(input('Digite sua idade: '))
if (idade < 3):
    print('Entrada gratuita')
elif (idade >= 3 and idade <=12):
    print('entrada = R$10,00')
elif (idade >= 13 and idade <= 59):
    print('Entrada = R$15,00')
else:
    print('Entrada = R$12,00')
 
#Questão 5
num = int(input('Insira um número inteiro: '))
verif = num > 2
verif2 = num % 2 == 0
print(verif)
print(verif2)
if (verif2 == False and verif == True):
    print('Não divisível por 2, É um número primo')
else:
    print('É divisível por 2, NÃO é um número primo')
 
 