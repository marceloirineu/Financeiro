"""Este programa retorna os valores do salários líquidos após desconto sociais"""

salario_contribuinte = 3000


def inss (salario_bruto):
    return salario_bruto*0.2


def dependentes (numero_de_dependentes):
    return 100*numero_de_dependentes


def ir (salario_desconta):
    return salario_desconta * 0.05


def salario_liquido (salario_bruto):
    contribuicao = inss (salario_contribuinte) + dependentes (2)

    salario_desconta = salario_contribuinte - contribuicao

    return salario_liquido = salario_desconta - ir (salario_desconta)
