# INSIRA ABAIXO OS NOMES DOS ALUNOS DO GRUPO (máximo 5 alunos)
# ALUNO 1: Leonardo Andrade de Souza        
# ALUNO 2:
# ALUNO 3:
# ALUNO 4:
# ALUNO 5:


def calcular_salario(dicionario, nome):
    salario_l = 0
    
    
    ocupacao = dicionario[nome][2]
    salario_bruto = dicionario[nome][1]
    if ocupacao == 'DESENVOLVEDOR':
        if salario_bruto >= 2000:
            salario_l = salario_bruto - salario_bruto*0.15
        else:
            salario_l = salario_bruto - salario_bruto*0.05
    elif ocupacao == 'ANALISTA':
        if salario_bruto >= 3500:
            salario_l = salario_bruto - salario_bruto*0.20
        else:
            salario_l = salario_bruto - salario_bruto*0.10
    elif ocupacao == 'GERENTE':
        if salario_bruto >= 4000:
            salario_l = salario_bruto - salario_bruto*0.25
        else:
            salario_l = salario_bruto - salario_bruto*0.15
    else:
        if nome not in dicionario:
            raise KeyError
        if ocupacao != 'DESENVOLVEDOR'or 'ANALISTA'or'GERENTE':
            raise TypeError
    return salario_l