nome = input('Qual seu nome? ')
conta_1 = float(input('O valor da conta 1 é: '))
conta_2 = float(input('O valor da conta 2 é: '))
salário_geral = float(input('Qual seu salário? '))
multa = (conta_1 * 1.02) + (conta_2 * 1.02)
salário_restante = salário_geral - multa
print('O salário restante de', nome, 'é igual a R$ %6.2f' % salário_restante)

