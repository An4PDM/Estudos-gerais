# exemplo 1
dias_semana = ['segunda-feira', 'terça-feira', 'quarta-feira']
i = 0
while dias_semana:
    if i == 2:
        print("O dia da semana que corresponde a posição", i, "da lista dias_semana é:", dias_semana[i])
        break
    i += 2
# PASS - Passa a condição adiante;
# CONTINUE - 'Pula' a condição;
#BREAK - Dá fim à condição
