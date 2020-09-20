# INSIRA ABAIXO OS NOMES DOS ALUNOS DO GRUPO (máximo 5 alunos)
# ALUNO 1: Leonardo Andrade de Souza        
# ALUNO 2:
# ALUNO 3:
# ALUNO 4:
# ALUNO 5:


try:
    if nome not in dicio: 
        raise KeyError ('O nome não se encontra no dicionário!')
    if nome[2] != 'DESENVOLVEDOR'or 'ANALISTA'or'GERENTE':
        raise TypeError ('Cargo não existente!')
    def calcular_salario(dicionario, nome):
        for x in dicio:
            if nome[1] == 'DESENVOLVEDOR':
                if nome[1] >= 2.000:
                    desconto_desenvolvedor = (nome[1]*15)/100
                    return desconto_desenvolvedor
                elif nome[1] < 2.000:
                    desconto_desenvolvedor = (nome[1]*5)/100
                    return desconto_desenvolvedor
            elif nome[1] == 'ANALISTA':
                if nome[1] >= 3.500:
                    desconto_analista = (nome[1]*20)/100
                    return desconto_analista
                elif nome[1] < 3.500:
                    desconto_analista = (nome[1]*10)/100
                    return desconto_analista
            elif nome[1] == 'GERENTE':
                if nome[1] >= 4.000:
                    desconto_gerente = (nome[1]*25)/100
                    return desconto_gerente
                elif nome[1] < 2.000:
                        desconto_gerente = (nome[1]*15)/100
                        return desconto_gerente
                        break