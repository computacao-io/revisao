"""
Classe Funcionário:
Implemente a classe Funcionário.
Um empregado tem um nome (um string) e um salário(um float).

Escreva um construtor com dois parâmetros (nome e salário),
métodos para devolver nome, salário e para aumentar o salário
ao qual aumente em uma certa porcentagem.
"""


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = float(salario)

    def obter_nome(self):
        return self.nome

    def obter_salario(self):
        return self.salario

    def aumentar_salario(self, porcentagem):
        novo_salario = self.salario + (porcentagem/100 * self.salario)
        self.salario = novo_salario
