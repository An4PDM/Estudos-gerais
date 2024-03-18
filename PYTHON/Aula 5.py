#Questão 1
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
média = (nota1 + nota2)/ 2
if (média >=5):
    print('Aprovado')
else: 
   if (média >=3):
       print('Exame')
   else:
       print('Reprovado')

#Questão 2
cargo = float(input('Digite o código de seu cargo: '))
if (cargo == 1):
    print('Escritutário')
elif (cargo == 2):
    print('Secretária')
elif (cargo == 3):
    print('Caixa')
elif (cargo == 4):
    print('Gerente')
elif (cargo == 5):
    print('Diretor')
else:
    print('Código inválido')

#Questão 3
idade = float(input('Qual sua idade? '))
if (idade < 16):
    print('Não-eleitor')
elif (idade >=18 and idade<=65):
    print('Eleitor obrigatório')
else:
    print('Eleitor facultativo')

#Questão 4 
num1 = float(input('Digite um valor: '))
num2 = float(input('Digite outro valor: '))
menu = float(input('Para soma, digite 1 \nPara multiplicação, digite 2 \nPara subtração, digite 3 \nPara divisão, digite 4: '))
if (menu == 1):
    soma = num1 + num2
    print(soma)
elif (menu == 2):
    multiplicação = num1 * num2
    print(multiplicação)
elif (menu == 3):
    subtração = num1 - num2
    print(subtração)
elif (menu == 4):
    divisão = num1 / num2
    print(divisão)
else:
    print('Código inválido')

#Questão 5
nome = input('Qual seu nome? ')
tipo_apê = input( 'Qual o tipo de apartamento (a,b,c ou d)? ')
diárias = float(input('Digite o número de diárias: '))
con_interno = float(input('Qual será o seu consumo interno?'))
if (tipo_apê == 'a'):
    valor = 150
elif (tipo_apê == 'b'):
    valor = 100
elif (tipo_apê == 'c'):
    valor = 75
elif (tipo_apê == 'd'):
    valor = 50
else:
    print('Código inválido')

subtotal = (valor * diárias) + con_interno
print('O subtotal é R$%.2f'%subtotal)
taxa_serviço = subtotal * 10/100
print('A taxa de serviço é R$%.2f'%taxa_serviço)
total_geral = taxa_serviço + subtotal
print('O total geral da conta do(a) hospede', nome, 'é R$%.2f'%total_geral)

#Questão 6
p = float(input('Escreva a quantidade de peixes em KG pescados hoje: '))
if (p>50):
    e = p - 50
    m = e*4
    print('O total a pagar com a multa será R$%.2f' % m)
else:
    e = 0
    m = 0
    print('m =', m ,'e','e =', e)

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

#Questão 8
h = float(input('Qual a sua altura? '))
sexo = input('Qual o seu sexo? Digite fem ou masc: ')
if (sexo == 'fem'):
    peso_ideal = (62.1*h) - 44.7
    print('O seu peso ideal é %.2f'% peso_ideal, 'kg')
elif (sexo == 'masc'):
    peso_ideal = (72.7*h) - 58
    print('O seu peso ideal é %.2f'% peso_ideal, 'kg')

#Questão 9


